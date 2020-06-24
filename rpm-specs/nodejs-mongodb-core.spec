%global npm_name mongodb-core

%{?nodejs_find_provides_and_requires}

Summary:       Core MongoDB driver functionality
Name:          nodejs-%{npm_name}
Version:       1.2.32
Release:       9%{?dist}
License:       ASL 2.0
URL:           https://github.com/christkv/mongodb-core
Source0:       http://registry.npmjs.org/%{npm_name}/-/%{npm_name}-%{version}.tgz
BuildRequires: nodejs-devel
BuildArch:     noarch
ExclusiveArch: %{nodejs_arches} noarch

%description
Core MongoDB driver functionality, no bells and whistles
and meant for integration not end applications

The MongoDB Core driver is the low level part of the 2.0
or higher MongoDB driver and is meant for library developers
not end users. It does not contain any abstractions or
helpers outside of the basic management of MongoDB topology
connections, CRUD operations and authentication.

%prep
%setup -q -n package

%build
#nothing to do

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pr index.js lib package.json %{buildroot}%{nodejs_sitelib}/%{npm_name}


%files
%doc HISTORY.md README.md TESTING.md
%license LICENSE
%{nodejs_sitelib}/%{npm_name}

%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.32-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.32-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.32-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.32-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.32-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.32-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.32-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.32-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Jan 12 2016 Troy Dawson <tdawson@redhat.com> - 1.2.32-1
- Update to 1.2.32

* Wed Jul 22 2015 Troy Dawson <tdawson@redhat.com> - 1.2.7-2
- Spec file cleanup

* Mon Jul 20 2015 Troy Dawson <tdawson@redhat.com> - 1.2.7-1
- Updated to 1.2.7

* Thu May 07 2015 Troy Dawson <tdawson@redhat.com> - 1.1.26-1
- Initial build

