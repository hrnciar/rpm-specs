%global npm_name bson
# Although there are tests
# the dependancies aren't in Fedora yet
%global enable_tests 0

%{?nodejs_find_provides_and_requires}

Summary:       A bson parser for node.js and the browser
Name:          nodejs-%{npm_name}
Version:       0.4.23
Release:       10%{?dist}
License:       ASL 2.0
URL:           https://github.com/mongodb/js-bson
Source0:       http://registry.npmjs.org/%{npm_name}/-/%{npm_name}-%{version}.tgz
%if 0%{?enable_tests}
## To get the tests (Source1), do the following
# git clone https://github.com/mongodb/js-bson.git
# cd js-bson/
# tar cfz nodejs-bson-test-0.3.1.tar.gz test/
Source1:       nodejs-bson-test-0.3.1.tar.gz
%endif
BuildRequires: nodejs-packaging
%if 0%{?enable_tests}
BuildRequires: npm(gleak)
BuildRequires: npm(nodeunit)
BuildRequires: npm(one)
%endif
BuildArch:     noarch
ExclusiveArch: %{nodejs_arches} noarch

%description
A JS/C++ Bson parser for node, used in the MongoDB Native driver.

%prep
%setup -q -n package

%build
#nothing to do

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pr lib package.json %{buildroot}%{nodejs_sitelib}/%{npm_name}


%if 0%{?enable_tests}
%check
tar xfz %{SOURCE1}
nodeunit ./test/node && TEST_NATIVE=TRUE nodeunit ./test/node
%endif

%files
%doc HISTORY README.md
%license LICENSE
%{nodejs_sitelib}/%{npm_name}

%changelog
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.23-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.23-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.23-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.23-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.23-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.23-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.23-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Feb 19 2017 Piotr Popieluch <piotr1212@gmail.com> - 0.4.23-3
- FTBFS: update nodejs_arches and br: nodejs-devel -> nodejs-packaging

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.23-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Apr 28 2016 Troy Dawson <tdawson@redhat.com> - 0.4.23-1
- Update to 0.4.23

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.21-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Jan 12 2016 Troy Dawson <tdawson@redhat.com> - 0.4.21-1
- Update to 0.4.21

* Fri Dec 11 2015 Troy Dawson <tdawson@redhat.com> - 0.4.20-1
- Update to 0.4.20

* Mon Sep 21 2015 Troy Dawson <tdawson@redhat.com> - 0.4.12-1
- Update to 0.4.12

* Mon Jul 27 2015 Troy Dawson <tdawson@redhat.com> - 0.4.8-1
- Update to 0.4.8

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue May 05 2015 Troy Dawson <tdawson@redhat.com> - 0.3.1-1
- Updated to latest release
- Change from arch to noarch (Upstream made this change at 0.3.0)

* Wed Feb 25 2015 Troy Dawson <tdawson@redhat.com> - 0.2.19-1
- Updated to latest release

* Thu Jan 22 2015 Troy Dawson <tdawson@redhat.com> - 0.2.18-1
- Updated to latest release

* Fri Oct 24 2014 Troy Dawson <tdawson@redhat.com> - 0.2.15-1
- Updated to latest release

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Fri Jun 13 2014 Troy Dawson <tdawson@redhat.com> - 0.2.9-1
- Update to 0.2.9

* Mon Jun 09 2014 Troy Dawson <tdawson@redhat.com> - 0.2.8-3
- Fix for nan dependency

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri May 16 2014 Troy Dawson <tdawson@redhat.com> - 0.2.8-1
- Update to 0.2.8
- nan 1.0.0 or greater required for building

* Wed Mar 05 2014 Troy Dawson <tdawson@redhat.com> - 0.2.7-1
- Update to 0.2.7
- nan 0.8.0 or greater required for building

* Wed Feb 19 2014 Troy Dawson <tdawson@redhat.com> - 0.2.6-1
- Update to version 0.2.6
- nan required again for building.

* Fri Feb 14 2014 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.2.5-3
- rebuild for icu-53 (via v8)

* Thu Feb 06 2014 Troy Dawson <tdawson@redhat.com> - 0.2.5-2
- nan is no longer required for building.

* Thu Feb 06 2014 Troy Dawson <tdawson@redhat.com> - 0.2.5-1
- Update to version 0.2.5
- add nodejs exclusive arch

* Fri Jan 03 2014 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.2.3-4
- add macro to invoke dependency generator on EL6

* Tue Dec 03 2013 Troy Dawson <tdawson@redhat.com> - 0.2.3-3
- Fixed permission on bson.node

* Sat Nov 16 2013 Troy Dawson <tdawson@redhat.com> - 0.2.3-2
- Updated source

* Tue Oct 08 2013 Troy Dawson <tdawson@redhat.com> - 0.2.3-1
- Updated to 0.2.3
- Updated BuildRequires and added NODE_PATH
- Added testing, though set to false until packages are made.

* Tue Oct 08 2013 Troy Dawson <tdawson@redhat.com> - 0.2.2-1
- Updated to 0.2.2
- Updated spec file to Fedora guidelines

* Wed Apr 17 2013 Haibo Lin <hlin@redhat.com> - 0.1.8-1
- Initial build
