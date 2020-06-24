%{?nodejs_find_provides_and_requires}

%global enable_tests 1

Name:       nodejs-sax
Version:    0.6.0
Release:    11%{?dist}
Summary:    A streaming SAX-style XML parser in JavaScript for Node.js
License:    BSD and W3C
URL:        https://github.com/isaacs/sax-js
Source0:    http://registry.npmjs.org/sax/-/sax-%{version}.tgz

BuildArch:  noarch
%if 0%{?fedora} >= 19
ExclusiveArch: %{nodejs_arches} noarch
%else
ExclusiveArch: %{ix86} x86_64 %{arm} noarch
%endif

BuildRequires:  nodejs-packaging

%description
This is a SAX-style streaming XML parser in JavaScript for Node.js.

It is:
 - A very simple tool to parse through an XML string.
 - A stepping stone to a streaming HTML parser.
 - A handy way to deal with RSS and other mostly-ok-but-kinda-broken XML docs.


%prep
%setup -q -n package


%build
#nothing to do


%install
mkdir -p %{buildroot}%{nodejs_sitelib}/sax
cp -pr package.json lib/ %{buildroot}%{nodejs_sitelib}/sax
rm -f examples/switch-bench.js

%nodejs_symlink_deps


%if 0%{?enable_tests}
%check
%__nodejs test/index.js
%endif


%files
%doc AUTHORS LICENSE LICENSE-W3C.html README.md examples/
%{nodejs_sitelib}/sax


%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Apr 19 2014 Jamie Nguyen <jamielinux@fedoraproject.org> - 0.6.0-1
- update to upstream release 0.6.0

* Mon Aug 26 2013 Jamie Nguyen <jamielinux@fedoraproject.org> - 0.5.5-1
- update to upstream release 0.5.5

* Sun Jul 28 2013 Jamie Nguyen <jamielinux@fedoraproject.org> - 0.5.4-2
- restrict to compatible arches

* Sat May 25 2013 Jamie Nguyen <jamielinux@fedoraproject.org> - 0.5.4-1
- update to upstream release 0.5.4

* Thu Feb 21 2013 Jamie Nguyen <jamielinux@fedoraproject.org> - 0.5.2-1
- project relicensed from MIT to BSD
- include newly distributed LICENSE-w3C.html

* Wed Feb 20 2013 Jamie Nguyen <jamielinux@fedoraproject.org> - 0.5.1-2
- fix %%summary and %%description
- add W3C license

* Mon Feb 11 2013 Jamie Nguyen <jamielinux@fedoraproject.org> - 0.5.1-1
- initial package
