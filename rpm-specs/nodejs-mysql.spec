%global npm_name mysql
# Although there are tests
# the dependancies aren't in Fedora yet
%global enable_tests 0

%{?nodejs_find_provides_and_requires}

Summary:       A node.js driver for mysql
Name:          nodejs-%{npm_name}
Version:       2.18.1
Release:       2%{?dist}
License:       MIT and ISC
URL:           http://github.com/felixge/node-mysql
Source0:       http://registry.npmjs.org/%{npm_name}/-/%{npm_name}-%{version}.tgz
Source1:       %{npm_name}-%{version}-nm-prod.tgz
Source2:       %{npm_name}-%{version}-nm-dev.tgz
BuildRequires: nodejs-packaging
BuildArch:     noarch
ExclusiveArch: %{nodejs_arches} noarch

%description
This is a node.js driver for mysql.
It is written in JavaScript, does not require compiling, 
and is 100% MIT licensed.

%prep
%setup -q -n package

%build
#nothing to do

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pr index.js lib package.json %{buildroot}%{nodejs_sitelib}/%{npm_name}

# Setup bundled node modules
tar xfz %{SOURCE1}
mkdir -p node_modules
pushd node_modules
ln -s ../node_modules_prod/* .
popd
cp -pr node_modules node_modules_prod %{buildroot}%{nodejs_sitelib}/%{npm_name}

%check
%nodejs_symlink_deps --check
%if 0%{?enable_tests}
tar xfz %{SOURCE2}
pushd node_modules
ln -s ../node_modules_dev/* .
popd
ln -s ../../node_modules_dev/.bin/ .
make test
%endif

%files
%doc Changes.md Readme.md
%license License
%{nodejs_sitelib}/%{npm_name}

%changelog
* Thu Sep 17 2020 Troy Dawson <tdawson@redhat.com> - 2.18.1-2
- No need for nodejs_fixdep with bundling

* Thu Sep 17 2020 Troy Dawson <tdawson@redhat.com> - 2.18.1-1
- Update to 2.18.1
- Use bundling for runtime deps

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.10.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.10.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.10.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.10.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.10.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.10.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.10.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.10.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Dec 22 2016 Tom Hughes <tom@compton.nu> - 2.10.1-3
- Update supported architectures

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.10.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Jan 12 2016 Troy Dawson <tdawson@redhat.com> - 2.10.1-1
- Update to 2.10.1

* Mon Sep 21 2015 Troy Dawson <tdawson@redhat.com> - 2.9.0-1
- Update to 2.9.0

* Mon Sep 21 2015 Troy Dawson <tdawson@redhat.com> - 2.9.0-1
- Update to 2.9.0

* Mon Jul 27 2015 Troy Dawson <tdawson@redhat.com> - 2.8.0-1
- Update to 2.8.0

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.6.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue May 05 2015 Troy Dawson <tdawson@redhat.com> - 2.6.2-1
- Updated to latest release

* Wed Feb 25 2015 Troy Dawson <tdawson@redhat.com> - 2.5.5-1
- Updated to latest release

* Thu Jan 22 2015 Troy Dawson <tdawson@redhat.com> - 2.5.4-1
- Updated to latest release

* Fri Oct 24 2014 Troy Dawson <tdawson@redhat.com> - 2.5.2-1
- Updated to latest release

* Mon Jun 09 2014 Troy Dawson <tdawson@redhat.com> - 2.3.2-1
- Update to version 2.3.2

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed May 28 2014 Troy Dawson <tdawson@redhat.com> - 2.3.1-1
- Update to version 2.3.1

* Tue Apr 29 2014 Troy Dawson <tdawson@redhat.com> - 2.2.0-1
- Update to version 2.2.0

* Fri Mar 14 2014 Troy Dawson <tdawson@redhat.com> - 2.1.1-1
- Update to version 2.1.1

* Thu Feb 20 2014 Troy Dawson <tdawson@redhat.com> - 2.1.0-1
- Update to version 2.1.0

* Fri Feb 07 2014 Troy Dawson <tdawson@redhat.com> - 2.0.1-2
- readable-stream not needed in nodejs >= 0.10

* Thu Feb 06 2014 Troy Dawson <tdawson@redhat.com> - 2.0.1-1
- Update to version 2.0.1
- add nodejs exclusive arch
- add macro to invoke dependency generator on EL6

* Thu Oct 10 2013 Troy Dawson <tdawson@redhat.com> - 2.0.0-alpha9.2
- Fix require-all dependancy to work with version in Fedora

* Thu Oct 03 2013 Troy Dawson <tdawson@redhat.com> - 2.0.0-alpha9.1
- Updated to version 2.0.0-alpha9

* Tue May 21 2013 Troy Dawson <tdawson@redhat.com> - 2.0.0-alpha8.1
- Initial build

