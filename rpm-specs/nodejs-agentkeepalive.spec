%bcond_with internet

Name:           nodejs-agentkeepalive
Version:        3.5.2
Release:        3%{?dist}
Summary:        Missing keep-alive http.Agent

License:        MIT
URL:            https://github.com/node-modules/agentkeepalive
Source0:        https://github.com/node-modules/agentkeepalive/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source20:       nodejs-agentkeepalive-ssl.conf
# Remove tests that need internet access
Patch0:         nodejs-agentkeepalive-internet.patch
BuildArch:      noarch
ExclusiveArch:  %{nodejs_arches} noarch

BuildRequires:  nodejs-packaging

BuildRequires:  openssl
BuildRequires:  npm(mocha)
BuildRequires:  npm(humanize-ms)
BuildRequires:  npm(should)
BuildRequires:  npm(should-http)
BuildRequires:  npm(pedding)

%description
The nodejs's missing keep alive http.Agent. Support HTTP and HTTPS.


%prep
%setup -q -n agentkeepalive-%{version}
%if ! %{with internet}
%patch0 -p1
%endif
rm -rf node_modules


%build


%install
mkdir -p %{buildroot}/%{nodejs_sitelib}/agentkeepalive
cp -pr package.json index.js lib %{buildroot}/%{nodejs_sitelib}/agentkeepalive
%nodejs_symlink_deps


%check
%nodejs_symlink_deps --check
pushd test/fixtures
OPENSSL_CONF=%{SOURCE20} sh genkey.sh
popd
%{nodejs_sitelib}/mocha/bin/mocha -R spec -t 10000 -r should-http test/*.test.js


%files
%doc README.md History.md AUTHORS example
%{nodejs_sitelib}/agentkeepalive


%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Feb 19 2019 Tom Hughes <tom@compton.nu> - 3.5.2-1
- Update to 3.5.2 upstream release

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Aug  1 2018 Tom Hughes <tom@compton.nu> - 3.5.1-1
- Update to 3.5.1 upstream release

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Mar  9 2018 Tom Hughes <tom@compton.nu> - 3.4.1-1
- Update to 3.4.1 upstream release

* Tue Feb 27 2018 Tom Hughes <tom@compton.nu> - 3.4.0-1
- Update to 3.4.0 upstream release

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Jun 20 2017 Tom Hughes <tom@compton.nu> - 3.3.0-1
- Update to 3.3.0 upstream release

* Sat Jun 10 2017 Tom Hughes <tom@compton.nu> - 3.2.0-1
- Update to 3.2.0 upstream release

* Wed May  3 2017 Tom Hughes <tom@compton.nu> - 3.1.0-1
- Update to 3.1.0 upstream release

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Dec 20 2016 Tom Hughes <tom@compton.nu> - 3.0.0-1
- Update to 3.0.0 upstream release

* Sun Jun 26 2016 Tom Hughes <tom@compton.nu> - 2.2.0-1
- Update to 2.2.0 upstream release

* Sun Apr 10 2016 Tom Hughes <tom@compton.nu> - 2.1.1-1
- Update to 2.1.1 upstream release

* Sat Apr  2 2016 Tom Hughes <tom@compton.nu> - 2.1.0-1
- Update to 2.1.0 upstream release

* Wed Mar 16 2016 Tom Hughes <tom@compton.nu> - 2.0.5-1
- Update to 2.0.5 upstream release

* Mon Mar 14 2016 Tom Hughes <tom@compton.nu> - 2.0.4-1
- Update to to 2.0.4 upstream release

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Aug 26 2015 Tom Hughes <tom@compton.nu> - 2.0.3-1
- Update to 2.0.3 upstream release
- Switch to source from github to get tests

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Nov 19 2013 Tom Hughes <tom@compton.nu> - 0.2.2-1
- Update to 0.2.2 upstream release

* Fri Nov  8 2013 Tom Hughes <tom@compton.nu> - 0.2.0-1
- Update to 0.2.0 upstream release
- Update to latest nodejs packaging standards

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sun May 26 2013 Tom Hughes <tom@compton.nu> - 0.1.5-2
- Fix rpmlint warnings

* Mon Feb 25 2013 Tom Hughes <tom@compton.nu> - 0.1.5-1
- Initial build of 0.1.5
