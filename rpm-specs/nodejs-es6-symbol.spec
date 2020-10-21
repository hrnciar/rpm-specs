%{?nodejs_find_provides_and_requires}

%global packagename es6-symbol
%global enable_tests 0
# tests disabled due to missing npm(tad) test suite

Name:		nodejs-es6-symbol
Version:	3.1.0
Release:	10%{?dist}
Summary:	ECMAScript 6 Symbol polyfill

License:	MIT
URL:		https://github.com/medikoo/es6-symbol.git
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


%description
ECMAScript 6 Symbol polyfill


%prep
%setup -q -n package

%nodejs_fixdep d "<=2.0.0"
# allow either the 0.1.x or 1.x.x series of npm(d)

%build
# nothing to do!

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{packagename}
cp -pr package.json *.js \
	%{buildroot}%{nodejs_sitelib}/%{packagename}

%nodejs_symlink_deps

%check
%nodejs_symlink_deps --check
%{__nodejs} -e 'require("./")'
%if 0%{?enable_tests}
%{__nodejs} %{nodejs_sitelib}/tad/bin/tad
%else
echo "Tests have been disabled..."
%endif


%files
%{!?_licensedir:%global license %doc}
%doc *.md CHANGES
%license LICENSE
%{nodejs_sitelib}/%{packagename}



%changelog
* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.0-10
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Jul 14 2016 Jared Smith <jsmith@fedoraproject.org> - 3.1.0-1
- Update to upstream 3.1.0 release

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sun Dec 20 2015 Jared Smith <jsmith@fedoraproject.org> - 3.0.2-2
- Allow newer version of npm(d)

* Fri Dec 18 2015 Jared Smith <jsmith@fedoraproject.org> - 3.0.2-1
- Update to upstream 3.0.2 release
- disable self-test until we get all the run-time dependencies into Rawhide

* Tue Nov 10 2015 Jared Smith <jsmith@fedoraproject.org> - 3.0.1-1
- Initial packaging
