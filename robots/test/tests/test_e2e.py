from django.test import TestCase
from robots.models import AllowedUrl, DisallowedUrl, Rule
from wagtail.models import Site


class TestE2E(TestCase):
    def test_robots_txt_defaults(self):
        response = self.client.get("/robots.txt")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response["Content-Type"], "text/plain")
        self.assertContains(response, "User-agent: *")
        self.assertContains(response, "Disallow: /admin")
        self.assertContains(response, "Host: localhost")

    def test_robots_txt_allows(self):
        rule = Rule.objects.create(
            robot="FooBot",
        )
        AllowedUrl.objects.create(rule=rule, pattern="/foo")
        AllowedUrl.objects.create(rule=rule, pattern="/bar")
        response = self.client.get("/robots.txt")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response["Content-Type"], "text/plain")
        self.assertContains(response, "User-agent: FooBot")
        self.assertContains(response, "Allow: /foo")
        self.assertContains(response, "Allow: /bar")
        self.assertContains(response, "Host: localhost")
        self.assertNotContains(response, "Disallow: /admin")

    def test_robots_txt_disallows(self):
        rule = Rule.objects.create(
            robot="FooBot",
        )
        DisallowedUrl.objects.create(rule=rule, pattern="/foo")
        DisallowedUrl.objects.create(rule=rule, pattern="/bar")
        response = self.client.get("/robots.txt")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response["Content-Type"], "text/plain")
        self.assertContains(response, "User-agent: FooBot")
        self.assertContains(response, "Disallow: /foo")
        self.assertContains(response, "Disallow: /bar")
        self.assertContains(response, "Host: localhost")
        self.assertNotContains(response, "Disallow: /admin")

    def test_robots_txt_disallows_and_allows(self):
        rule = Rule.objects.create(
            robot="FooBot",
        )
        DisallowedUrl.objects.create(rule=rule, pattern="/foo")
        DisallowedUrl.objects.create(rule=rule, pattern="/bar")
        AllowedUrl.objects.create(rule=rule, pattern="/baz")
        response = self.client.get("/robots.txt")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response["Content-Type"], "text/plain")
        self.assertContains(response, "User-agent: FooBot")
        self.assertContains(response, "Disallow: /foo")
        self.assertContains(response, "Disallow: /bar")
        self.assertContains(response, "Allow: /baz")
        self.assertContains(response, "Host: localhost")
        self.assertNotContains(response, "Disallow: /admin")

    def test_robots_txt_host(self):
        site = Site.objects.get(is_default_site=True)
        site.hostname = "foo.com"
        site.save()
        response = self.client.get("/robots.txt")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response["Content-Type"], "text/plain")
        self.assertContains(response, "Host: foo.com")
