%global npm_name node-static
%global enable_tests 0

%{?nodejs_find_provides_and_requires}

Summary:       Simple, compliant file streaming module for node
Name:          nodejs-%{npm_name}
Version:       0.7.8
Release:       9%{?dist}
License:       MIT
URL:           http://github.com/cloudhead/node-static
Source0:       http://registry.npmjs.org/%{npm_name}/-/%{npm_name}-%{version}.tgz
BuildRequires: nodejs-devel
%if 0%{?enable_tests}
BuildRequires: npm(vows)
%endif
BuildArch:     noarch
ExclusiveArch: %{nodejs_arches} noarch

%description
node-static is a simple, "rfc 2616 compliant" file streaming module 
for node.

node-static has an in-memory file cache, making it highly efficient.
node-static understands and supports "conditional GET" and "HEAD" requests.
node-static was inspired by some of the other static-file serving modules
out there, such as node-paperboy and antinode.

%prep
%setup -q -n package

%build
#nothing to do

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pr benchmark bin examples lib package.json test %{buildroot}%{nodejs_sitelib}/%{npm_name}

# Setup Binaries
mkdir %{buildroot}%{_bindir}
ln -s %{nodejs_sitelib}/%{npm_name}/bin/cli.js %{buildroot}%{_bindir}/static

%if 0%{?enable_tests}
%check
%nodejs_symlink_deps --check
vows --spec --isolate
%endif

%files
%doc README.md
%license LICENSE
%{nodejs_sitelib}/%{npm_name}
%{_bindir}/static

%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.8-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.8-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.8-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.8-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.8-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.8-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Dec 22 2016 Tom Hughes <tom@compton.nu> - 0.7.8-2
- Update supported architectures

* Fri Sep 09 2016 Troy Dawson <tdawson@redhat.com> - 0.7.8-1
- Update to 0.7.8

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Jul 27 2015 Troy Dawson <tdawson@redhat.com> - 0.7.7-1
- Update to 0.7.7

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Oct 24 2014 Troy Dawson <tdawson@redhat.com> - 0.7.6-1
- Updated to latest release

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Feb 06 2014 Troy Dawson <tdawson@redhat.com> - 0.7.3-1
- Update to version 0.7.3
- add nodejs exclusive arch
- add macro to invoke dependency generator on EL6

* Fri Oct 11 2013 Troy Dawson <tdawson@redhat.com> - 0.7.1-2
- Cleaned up description

* Tue Oct 08 2013 Troy Dawson <tdawson@redhat.com> - 0.7.1-1
- Updated to 0.7.1

* Thu Feb 16 2012 Troy Dawson <tdawson@redhat.com> - 0.6.9-1
- Initial build

