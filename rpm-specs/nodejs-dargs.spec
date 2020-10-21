%{?nodejs_find_provides_and_requires}

%global packagename dargs

# tests missing due to missing npm(ava)
%global enable_tests 0

Name:		nodejs-dargs
Version:	5.1.0
Release:	8%{?dist}
Summary:	Convert an object of options into an array of command-line arguments

License:	MIT
URL:		https://github.com/sindresorhus/dargs
Source0:	https://registry.npmjs.org/%{packagename}/-/%{packagename}-%{version}.tgz
Source1:	https://raw.githubusercontent.com/sindresorhus/%{packagename}/v%{version}/test.js


ExclusiveArch:	%{nodejs_arches} noarch
BuildArch:	noarch

BuildRequires:	nodejs-packaging
%if 0%{?enable_tests}
BuildRequires:	npm(ava)
%endif

%description
Reverse minimist. Convert an object of options into an array of command-line
arguments.


%prep
%autosetup -n package
# setup the tests
cp -p %{SOURCE1} .

%build
# nothing to do!

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{packagename}
cp -pr package.json index.js \
	%{buildroot}%{nodejs_sitelib}/%{packagename}

%nodejs_symlink_deps

%check
%nodejs_symlink_deps --check
%{__nodejs} -e 'require("./")'
%if 0%{?enable_tests}
%{_bindir}/ava
%else
%{_bindir}/echo -e "\e[101m -=#=- Tests disabled -=#=- \e[0m"
%endif

%files
%doc readme.md
%license license
%{nodejs_sitelib}/%{packagename}

%changelog
* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.1.0-8
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.1.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.1.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 5.1.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 5.1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 5.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 5.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sun May  7 2017 Jared Smith <jsmith@fedoraproject.org> - 5.1.0-1
- Initial packaging
