Name:           nodejs-speedometer
Version:        1.0.0
Release:        9%{?dist}
Summary:        Simple speed measurement in Javascript

License:        MIT
URL:            https://github.com/mafintosh/speedometer
Source0:        http://registry.npmjs.org/speedometer/-/speedometer-%{version}.tgz
BuildArch:      noarch
ExclusiveArch:  %{nodejs_arches} noarch

BuildRequires:  nodejs-packaging

%description
Simple speed measurement in Javascript.


%prep
%setup -q -n package
rm -rf node_modules


%build


%install
mkdir -p %{buildroot}%{nodejs_sitelib}/speedometer
cp -pr package.json index.js %{buildroot}%{nodejs_sitelib}/speedometer
%nodejs_symlink_deps


%files
%doc README.md
%license LICENSE
%{nodejs_sitelib}/speedometer


%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Oct 16 2015 Tom Hughes <tom@compton.nu> - 1.0.0-1
- Update to 1.0.0 upstream release
- Switch to %%license for the license file

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Jan  4 2015 Tom Hughes <tom@compton.nu> - 0.1.4-1
- Update to 0.1.4 upstream release

* Mon Jun 30 2014 Tom Hughes <tom@compton.nu> - 0.1.3-1
- Update to 0.1.3 upstream release

* Mon Jun 30 2014 Tom Hughes <tom@compton.nu> - 0.1.2-1
- Initial build of 0.1.2
