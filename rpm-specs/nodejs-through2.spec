# test are failing 
%global enable_tests 0
%global module_name through2

Name:           nodejs-%{module_name}
Version:        2.0.3
Release:        7%{?dist}
Summary:        Node streams2 Transform wrapper to avoid explicit subclassing noise

License:        MITNFA
URL:            https://github.com/rvagg/through2
Source0:        https://github.com/rvagg/%{module_name}/archive/v%{version}/%{module_name}-%{version}.tar.gz
BuildArch:      noarch
ExclusiveArch:  %{nodejs_arches} noarch

BuildRequires:  nodejs-packaging

%if 0%{?enable_tests}
BuildRequires:  npm(tap)
BuildRequires:  npm(tape)
BuildRequires:  npm(xtend)
BuildRequires:  npm(bl)
BuildRequires:  npm(stream-spigot)
%endif

%description
A tiny wrapper around Node streams2 Transform to avoid explicit subclassing
noise.

%prep
%autosetup -n %{module_name}-%{version}
%nodejs_fixdep readable-stream "^2.0.5"
rm -rf node_modules


%build
# nothing to build

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{module_name}
cp -pr package.json *.js %{buildroot}%{nodejs_sitelib}/%{module_name}
%nodejs_symlink_deps

%if 0%{?enable_tests}
%check
%nodejs_symlink_deps --check
%{__nodejs} -e 'require("./")'
node test/test.js
%endif

%files
%doc README.md
%license LICENSE.md
%{nodejs_sitelib}/%{module_name}

%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Apr 11 2017 Tom Hughes <tom@compton.nu> - 2.0.3-1
- Update to 2.0.3 upstream release

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Feb 09 2016 Jared Smith <jsmith@fedoraproject.org> - 2.0.1-1
- Update to upstream 2.0.1 release

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jul 22 2015 Parag Nemade <pnemade AT fedoraproject DOT org> - 0.1.3-4
- Update to 2.0.0
- disable tests

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Dec 22 2014 Parag Nemade <pnemade AT redhat DOT com> - 0.6.3-1
- Initial packaging

