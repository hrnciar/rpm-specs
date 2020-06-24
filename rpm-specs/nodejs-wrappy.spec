%{?nodejs_find_provides_and_requires}

%global enable_tests 1
%global module_name wrappy

Name:       nodejs-wrappy
Version:    1.0.2
Release:    8%{?dist}
Summary:    Callback wrapping utility
License:    ISC
URL:        https://github.com/npm/wrappy
Source0:    https://github.com/npm/wrappy/archive/v%{version}.tar.gz

BuildArch:  noarch

BuildRequires:  nodejs-packaging

%if 0%{?enable_tests}
BuildRequires:  npm(tap)
%endif

ExclusiveArch: %{nodejs_arches} noarch

%description
Callback wrapping utility for node.js

%prep
%setup -q -n wrappy-%{version}

%build
#nothing to do

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{module_name}
cp -pr wrappy.js package.json \
    %{buildroot}%{nodejs_sitelib}/%{module_name}

%{nodejs_symlink_deps}

%if 0%{?enable_tests}
%check
%{nodejs_symlink_deps} --check
tap test/*.js
%endif

%files
%doc README.md
%license LICENSE
%{nodejs_sitelib}/%{module_name}

%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Oct 17 2016 Anish Patil <anish.developer@gmail.com> - 1.0.2-1
- Upstream has released new version

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Apr 15 2015 Parag Nemade <pnemade AT redhat DOT com> - 1.0.1-3
- Use correct github source guidelines
- Use correct module name directory

* Sun Apr 12 2015 Parag Nemade <pnemade AT redhat DOT com> - 1.0.1-2
- Some spec cleanup to follow nodejs packaging guidelines
- Add missing macro in %%check

* Thu Nov 06 2014 Anish Patil <apatil@redhat.com> - 1.0.1-1
- Initial package
