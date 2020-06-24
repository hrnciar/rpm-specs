Name:           nodejs-oauth
Version:        0.9.15
Release:        8%{?dist}
Summary:        Library for interacting with OAuth 1.0, 1.0A, 2 and Echo

License:        MIT
URL:            https://github.com/ciaranj/node-oauth
Source0:        http://registry.npmjs.org/oauth/-/oauth-%{version}.tgz
# Remove fallback to bundled SHA1 implementation
Patch0:         nodejs-oauth-sha1.patch
# https://github.com/ciaranj/node-oauth/pull/268
Patch1:         nodejs-oauth-network.patch
BuildArch:      noarch
ExclusiveArch:  %{nodejs_arches} noarch

BuildRequires:  nodejs-packaging

BuildRequires:  npm(vows)

%description
Library for interacting with OAuth 1.0, 1.0A, 2 and Echo. Provides
simplified client access and allows for construction of more complex
APIs and OAuth providers.


%prep
%setup -q -n package
%patch0 -p1
%patch1 -p1
rm -rf node_modules lib/sha1.js tests/sha1tests.js


%build


%install
mkdir -p %{buildroot}/%{nodejs_sitelib}/oauth
cp -pr package.json index.js lib %{buildroot}/%{nodejs_sitelib}/oauth
%nodejs_symlink_deps


%check
%nodejs_symlink_deps --check
%{nodejs_sitelib}/vows/bin/vows tests/*tests.js --spec


%files
%doc Readme.md examples
%license LICENSE
%{nodejs_sitelib}/oauth


%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.15-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.15-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.15-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.15-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.15-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.15-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.15-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Jan  5 2017 Tom Hughes <tom@compton.nu> - 0.9.15-1
- Update to 0.9.15 upstream release

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.14-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Oct 27 2015 Tom Hughes <tom@compton.nu> - 0.9.14-2
- Fix test failures with newer vows in no-network environment

* Wed Sep 23 2015 Tom Hughes <tom@compton.nu> - 0.9.14-1
- Update to 0.9.14 upstream release
- Switch to %%license for the license file

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.13-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun May 17 2015 Tom Hughes <tom@compton.nu> - 0.9.13-1
- Update to 0.9.13 upstream release

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.12-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri May 23 2014 Tom Hughes <tom@compton.nu> - 0.9.12-1
- Update to 0.9.12 upstream release

* Mon Jan  6 2014 Tom Hughes <tom@compton.nu> - 0.9.11-1
- Update to 0.9.11 upstream release
- Update to latest nodejs packaging standards

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sun Mar 10 2013 Tom Hughes <tom@compton.nu> - 0.9.10-1
- Update to 0.9.10 upstream release

* Sun Mar 10 2013 Tom Hughes <tom@compton.nu> - 0.9.8-4
- Remove fallback to bundled SHA1 implementation

* Sat Mar  9 2013 Tom Hughes <tom@compton.nu> - 0.9.8-3
- Replace bundled sha1.js with a dependency on jshashes
- Remove BSD from license

* Sat Mar  2 2013 Tom Hughes <tom@compton.nu> - 0.9.8-2
- Link node_modules for tests
- Improve description
- Add BSD to license

* Sun Feb 10 2013 Tom Hughes <tom@compton.nu> - 0.9.8-1
- Initial build of 0.9.8
