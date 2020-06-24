%global npm_name mongodb

%{?nodejs_find_provides_and_requires}

Summary:       A node driver for MongoDB
Name:          nodejs-%{npm_name}
Version:       2.1.18
Release:       9%{?dist}
License:       ASL 2.0
URL:           https://github.com/mongodb/node-mongodb-native
Source0:       http://registry.npmjs.org/%{npm_name}/-/%{npm_name}-%{version}.tgz
BuildRequires: nodejs-packaging
BuildArch:     noarch
ExclusiveArch: %{nodejs_arches} noarch

%description
This is a node driver for MongoDB. It's a port (or close to a port) of
the library for ruby at http://github.com/mongodb/mongo-ruby-driver

%prep
%setup -q -n package

%nodejs_fixdep mongodb-core '>=1.2.32'
%nodejs_fixdep readable-stream '>=1.0.31'
%nodejs_fixdep es6-promise '>=3.0.2'

%build
#nothing to do

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pr index.js lib package.json %{buildroot}%{nodejs_sitelib}/%{npm_name}

%files
%doc HISTORY.md
%license LICENSE
%{nodejs_sitelib}/%{npm_name}

%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.18-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.18-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.18-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.18-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.18-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.18-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Feb 19 2017 Piotr Popieluch <piotr1212@gmail.com> - 2.1.18-3
- Update BR: and ExclusiveArch to fix FTBFS

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.18-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Apr 28 2016 Troy Dawson <tdawson@redhat.com> - 2.1.18-1
- Update to 2.1.18

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Jan 12 2016 Troy Dawson <tdawson@redhat.com> - 2.1.4-1
- Update to 2.1.4

* Mon Sep 21 2015 Troy Dawson <tdawson@redhat.com> - 2.0.43-1
- Update to 2.0.43

* Mon Jul 27 2015 Troy Dawson <tdawson@redhat.com> - 2.0.39-1
- Update to 2.0.39

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.28-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu May 07 2015 Troy Dawson <tdawson@redhat.com> - 2.0.28-2
- Fix dependencies

* Tue May 05 2015 Troy Dawson <tdawson@redhat.com> - 2.0.28-1
- Updated to latest release

* Wed Feb 25 2015 Troy Dawson <tdawson@redhat.com> - 1.4.31-1
- Updated to latest release

* Thu Jan 22 2015 Troy Dawson <tdawson@redhat.com> - 1.4.29-1
- Updated to latest release

* Fri Oct 24 2014 Troy Dawson <tdawson@redhat.com> - 1.4.19-1
- Updated to latest release

* Thu Jul 03 2014 Troy Dawson <tdawson@redhat.com> - 1.4.7-1
- Update to version 1.4.7

* Fri Jun 13 2014 Troy Dawson <tdawson@redhat.com> - 1.4.6-1
- Update to version 1.4.6

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed May 28 2014 Troy Dawson <tdawson@redhat.com> - 1.4.5-1
- Update to version 1.4.5

* Mon Apr 21 2014 Troy Dawson <tdawson@redhat.com> - 1.4.2-1
- Update to version 1.4.2

* Thu Feb 06 2014 Troy Dawson <tdawson@redhat.com> - 1.3.23-1
- Update to version 1.3.23
- add nodejs exclusive arch

* Wed Jan 08 2014 Troy Dawson <tdawson@redhat.com> - 1.3.19-3
- Fix bson dependancy

* Fri Jan 03 2014 T.C. Hollingsworth <tchollingsworth@gmail.com> - 1.3.19-2
- add macro to invoke dependency generator on EL6

* Thu Oct 03 2013 Troy Dawson <tdawson@redhat.com> - 1.3.19-1
- Updated to version 1.3.19

* Fri Aug 09 2013 Troy Dawson <tdawson@redhat.com> - 1.3.17-1
- Updated to version 1.3.17
- Package using the new Fedora guidelines

* Wed Jul 24 2013 Troy Dawson <tdawson@redhat.com> - 1.3.12-1
- Updated to version 1.3.12

* Wed Apr 17 2013 Haibo Lin <hlin@redhat.com> - 1.2.14-1
- Build under eng-rhel-6 and update to upstream version 1.2.14

* Thu Feb 16 2012 Troy Dawson <tdawson@redhat.com> - 0.9.9.1-1
- Initial build

