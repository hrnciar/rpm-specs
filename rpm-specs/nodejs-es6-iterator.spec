%{?nodejs_find_provides_and_requires}

%global packagename es6-iterator
%global enable_tests 0
# tests disabled due to missing npm(tad) test suite

Name:		nodejs-es6-iterator
Version:	2.0.0
Release:	11%{?dist}
Summary:	Iterator abstraction based on ES6 specification

License:	MIT
URL:		https://github.com/medikoo/es6-iterator.git
Source0:	https://registry.npmjs.org/%{packagename}/-/%{packagename}-%{version}.tgz

BuildArch:	noarch
%if 0%{?fedora} >= 19
ExclusiveArch: %{nodejs_arches} noarch
%else
ExclusiveArch: %{ix86} x86_64 %{arm} noarch
%endif

BuildRequires:	nodejs-packaging
%if 0%{?enable_tests}
BuildRequires:	npm(tad)
%endif

Requires:	nodejs

%description
Iterator abstraction based on ES6 specification


%prep
%setup -q -n package

%nodejs_fixdep d "<=2.0.0"
# allow either the 0.1.x or 1.x.x series of npm(d) 


%build
# nothing to do!

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{packagename}
cp -pr package.json *.js \#/ \
	%{buildroot}%{nodejs_sitelib}/%{packagename}

%nodejs_symlink_deps

%check
%nodejs_symlink_deps --check
%if 0%{?enable_tests}
%{__nodejs} -e 'require("./")'
%{__nodejs} %{nodejs_sitelib}/tad/bin/tad
%else
echo "Tests are disabled..."
%endif


%files
%{!?_licensedir:%global license %doc}
%doc *.md CHANGES
%license LICENSE
%{nodejs_sitelib}/%{packagename}



%changelog
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Dec 22 2015 Jared Smith <jsmith@fedoraproject.org> - 2.0.0-2
- rebuilt to allow newer version of npm(d)

* Tue Nov 10 2015 Jared Smith <jsmith@fedoraproject.org> - 2.0.0-1
- Initial packaging
