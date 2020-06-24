%{?nodejs_find_provides_and_requires}

%global packagename gauge
%global enable_tests 1

Name:		nodejs-gauge
Version:	1.2.5
Release:	10%{?dist}
Summary:	A terminal based horizontal gauge

License:	ISC
URL:		https://github.com/iarna/gauge.git
Source0:	https://registry.npmjs.org/%{packagename}/-/%{packagename}-%{version}.tgz
# Update for lodash 4.x
Patch0:         nodejs-gauge-lodash.patch

BuildArch:	noarch
%if 0%{?fedora} >= 19
ExclusiveArch: %{nodejs_arches} noarch
%else
ExclusiveArch: %{ix86} x86_64 %{arm} noarch
%endif

BuildRequires:	nodejs-packaging
BuildRequires:	npm(ansi)
BuildRequires:	npm(has-unicode)
BuildRequires:	npm(lodash.pad)
BuildRequires:	npm(lodash.padstart)
BuildRequires:	npm(lodash.padend)
%if 0%{?enable_tests}
BuildRequires:	npm(tap)
%endif

%description
A terminal based horizontal gauge


%prep
%autosetup -p 1 -n package

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
%{_bindir}/tap test/*.js
%endif


%files
%{!?_licensedir:%global license %doc}
%doc *.md
%license LICENSE
%{nodejs_sitelib}/%{packagename}



%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.5-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Sep 14 2019 Tom Hughes <tom@compton.nu> - 1.2.5-9
- Rebuild against lodash 4.x

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.5-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.5-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Feb 01 2016 Jared Smith <jsmith@fedoraproject.org> - 1.2.5-1
- Update to upstream 1.2.5 release

* Wed Jan 13 2016 Jared Smith <jsmith@fedoraproject.org> - 1.2.4-1
- Update to upstream 1.2.4 release

* Wed Dec 16 2015 Jared Smith <jsmith@fedoraproject.org> - 1.2.2-1
- Initial packaging
