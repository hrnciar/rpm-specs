%{?nodejs_find_provides_and_requires}

%global packagename cli-color
%global enable_tests 0
# tests disabled due to dependency on npm(tad), which hasn't been packaged
# in Fedora, and has a circular dependency on this package

Name:		nodejs-cli-color
Version:	1.1.0
Release:	10%{?dist}
Summary:	Colors, formatting and other tools for the console

License:	MIT
URL:		https://github.com/medikoo/cli-color.git
Source0:	https://registry.npmjs.org/%{packagename}/-/%{packagename}-%{version}.tgz

BuildArch:	noarch
%if 0%{?fedora} >= 19
ExclusiveArch: %{nodejs_arches} noarch
%else
ExclusiveArch: %{ix86} x86_64 %{arm} noarch
%endif

BuildRequires:	nodejs-packaging
BuildRequires:	npm(ansi-regex)
BuildRequires:	npm(d)
BuildRequires:	npm(es5-ext)
BuildRequires:	npm(es6-iterator)
BuildRequires:	npm(memoizee)
BuildRequires:	npm(timers-ext)
%if 0%{?enable_tests}
BuildRequires:	npm(tad)
%endif

Requires:	nodejs

%description
Colors, formatting and other tools for the console


%prep
%setup -q -n package

%nodejs_fixdep d '<2.0.0'
# Use either 0.1.x or 1.x.x versions of npm(d)


%build
# nothing to do!

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{packagename}
cp -pr package.json *.js lib/ bin/ \
	%{buildroot}%{nodejs_sitelib}/%{packagename}

%nodejs_symlink_deps

%check
%nodejs_symlink_deps --check
%{__nodejs} -e 'require("./")'
%if 0%{?enable_tests}
%{_bindir}/tad
%endif


%files
%{!?_licensedir:%global license %doc}
%doc *.md examples/
%license LICENSE
%{nodejs_sitelib}/%{packagename}



%changelog
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Nov  6 2015 Jared Smith <jsmith@fedoraproject.org> - 1.1.0-1
- Initial packaging
