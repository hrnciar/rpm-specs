%{?nodejs_find_provides_and_requires}

%global enable_tests 0

Name:       nodejs-formidable
Version:    1.1.1
Release:    7%{?dist}
Summary:    A Node.js module for parsing form data, especially file uploads
License:    MIT
URL:        https://github.com/felixge/node-formidable
Source0:    https://github.com/felixge/node-formidable/archive/v%{version}/formidable-%{version}.tar.gz

BuildArch:  noarch
ExclusiveArch: %{nodejs_arches} noarch

BuildRequires:  nodejs-packaging

%if 0%{?enable_tests}
BuildRequires:  npm(findit)
BuildRequires:  npm(gently)
BuildRequires:  npm(hashish)
BuildRequires:  npm(urun)
BuildRequires:  npm(utest)
%endif

%description
This is a Node.js module for parsing form data, especially file uploads.
It was developed for Transloadit, a service focused on uploading and encoding
images and videos.

It offers:
 - Fast (~500mb/sec), non-buffering multipart parser
 - Automatically writing file uploads to disk
 - Low memory footprint
 - Graceful error handling
 - Very high test coverage


%prep
%autosetup -n node-formidable-%{version}
rm -rf node-gently/


%build
#nothing to do


%install
mkdir -p %{buildroot}%{nodejs_sitelib}/formidable
cp -pr package.json index.js lib/ \
    %{buildroot}%{nodejs_sitelib}/formidable

%nodejs_symlink_deps


%check
%{__nodejs} -e 'require("./")'

%if 0%{?enable_tests}
%__nodejs test/run.js
%endif


%files
%doc Readme.md
%license LICENSE
%{nodejs_sitelib}/formidable


%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Mar 31 2017 Piotr Popieluch <piotr1212@gmail.com> - 1.1.1-1
- Update to 1.1.1

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.14-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.14-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.14-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.14-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.14-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sun Jul 21 2013 Jamie Nguyen <jamielinux@fedoraproject.org> - 1.0.14-2
- restrict to compatible arches

* Sat May 25 2013 Jamie Nguyen <jamielinux@fedoraproject.org> - 1.0.14-1
- update to upstream release 1.0.14
- patch for node version now fixed upstream

* Wed Mar 20 2013 Jamie Nguyen <jamielinux@fedoraproject.org> - 1.0.13-1
- update to upstream release 1.0.13

* Fri Mar 15 2013 Jamie Nguyen <jamielinux@fedoraproject.org> - 1.0.12-1
- update to upstream release 1.0.12
- use LICENSE file that is now included in the tarball

* Thu Feb 21 2013 Jamie Nguyen <jamielinux@fedoraproject.org> - 1.0.11-3
- add copy of LICENSE from upstream

* Wed Feb 20 2013 Jamie Nguyen <jamielinux@fedoraproject.org> - 1.0.11-2
- add npm(urun) to BuildRequires

* Mon Feb 11 2013 Jamie Nguyen <jamielinux@fedoraproject.org> - 1.0.11-1
- initial package
