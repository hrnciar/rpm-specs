Name:           jsoup
Summary:        Java library for working with real-world HTML
Version:        1.13.1
Release:        1%{?dist}
License:        MIT

URL:            http://jsoup.org/

# ./generate-tarball.sh
Source0:        %{name}-%{version}.tar.gz
# The sources contain non-free scraped web pages as test data
Source1:        generate-tarball.sh

BuildArch:      noarch

BuildRequires:  maven-local
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)

%description
jsoup is a Java library for working with real-world HTML.
It provides a very convenient API for extracting and manipulating data,
using the best of DOM, CSS, and jquery-like methods.

jsoup implements the WHATWG HTML5 specification,
and parses HTML to the same DOM as modern browsers do.

 - scrape and parse HTML from a URL, file, or string
 - find and extract data, using DOM traversal or CSS selectors
 - manipulate the HTML elements, attributes, and text
 - clean user-submitted content against a safe white-list,
   to prevent XSS attacks
 - output tidy HTML

jsoup is designed to deal with all varieties of HTML found in the wild;
from pristine and validating, to invalid tag-soup;
jsoup will create a sensible parse tree.


%package javadoc
Summary:        Javadoc for %{name}

%description javadoc
API documentation for %{name}.

%prep
%setup -q -n %{name}-%{name}-%{version}

%pom_remove_plugin :animal-sniffer-maven-plugin
%pom_remove_plugin :maven-failsafe-plugin
%pom_remove_plugin :maven-javadoc-plugin

%build
%mvn_build -f

%install
%mvn_install

%files -f .mfiles
%doc README.md CHANGES
%license LICENSE

%files javadoc -f .mfiles-javadoc
%license LICENSE

%changelog
* Thu May 14 2020 Fabio Valentini <decathorpe@gmail.com> - 1.13.1-1
- Update to version 1.13.1.

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.12.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Oct 20 2019 Fabio Valentini <decathorpe@gmail.com> - 1.12.1-1
- Update to version 1.12.1.

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.11.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.11.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Jul 18 2018 Michael Simacek <msimacek@redhat.com> - 1.11.3-3
- Remove non-free scraped web pages from SRPM

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.11.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Apr 19 2018 Michael Simacek <msimacek@redhat.com> - 1.11.3-1
- Update to upstream version 1.11.3

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.11.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Nov 27 2017 Michael Simacek <msimacek@redhat.com> - 1.11.2-1
- Update to upstream version 1.11.2

* Mon Nov 06 2017 Michael Simacek <msimacek@redhat.com> - 1.11.1-1
- Update to upstream version 1.11.1

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu Jun 15 2017 Michael Simacek <msimacek@redhat.com> - 1.10.3-1
- Update to upstream version 1.10.3

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Jan 04 2017 Michael Simacek <msimacek@redhat.com> - 1.10.2-1
- Update to upstream version 1.10.2

* Wed Nov 02 2016 Michael Simacek <msimacek@redhat.com> - 1.10.1-1
- Update to upstream version 1.10.1

* Tue May 24 2016 Michael Simacek <msimacek@redhat.com> - 1.9.2-1
- Update to upstream version 1.9.2

* Mon Apr 18 2016 Michael Simacek <msimacek@redhat.com> - 1.9.1-1
- Update to upstream version 1.9.1

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Aug 04 2015 Michael Simacek <msimacek@redhat.com> - 1.8.3-1
- Update to upstream version 1.8.3

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Apr 14 2015 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.8.2-1
- Update to upstream version 1.8.2

* Mon Sep 29 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.8.1-1
- Update to upstream version 1.8.1

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed May 21 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.7.2-3
- Update to current packaging guidelines

* Tue Mar 04 2014 Stanislav Ochotnicky <sochotnicky@redhat.com> - 1.7.2-2
- Use Requires: java-headless rebuild (#1067528)

* Mon Aug 12 2013 Alexander Kurtakov <akurtako@redhat.com> 1.7.2-1
- Update to latest upstream.

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Feb 06 2013 Java SIG <java-devel@lists.fedoraproject.org> - 1.6.1-6
- Update for https://fedoraproject.org/wiki/Fedora_19_Maven_Rebuild
- Replace maven BuildRequires with maven-local

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Apr 04 2012 Jaromir Capik <jcapik@redhat.com> - 1.6.1-4
- Removing maven from Requires

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri Jul 22 2011 Jaromir Capik <jcapik@redhat.com> - 1.6.1-2
- Switching to sources from github

* Fri Jul 22 2011 Jaromir Capik <jcapik@redhat.com> - 1.6.1-1
- Initial package

