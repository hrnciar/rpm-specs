%{?nodejs_find_provides_and_requires}

%global packagename tslib
%global enable_tests 1

Name:		nodejs-tslib
Version:	1.11.1
Release:	1%{?dist}
Summary:	Runtime library for TypeScript helper functions

License:	ASL 2.0
URL:		https://github.com/Microsoft/tslib.git
Source0:	https://registry.npmjs.org/%{packagename}/-/%{packagename}-%{version}.tgz

BuildArch:	noarch
ExclusiveArch:  %{nodejs_arches} noarch

BuildRequires:	nodejs-packaging


%description
Runtime library for TypeScript helper functions


%prep
%autosetup -n package


%build
# nothing to do


%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{packagename}
cp -pr package.json *.js *.ts \
	%{buildroot}%{nodejs_sitelib}/%{packagename}

%nodejs_symlink_deps


%check
%nodejs_symlink_deps --check
%{__nodejs} -e 'require("./")'
%if 0%{?enable_tests}
%{_bindir}/echo -e "\e[102m -=#=- This package has no tests -=#=- \e[0m"
%else
%{_bindir}/echo -e "\e[101m -=#=- Tests disabled -=#=- \e[0m"
%endif


%files
%doc *.md
%license LICENSE.txt CopyrightNotice.txt
%{nodejs_sitelib}/%{packagename}


%changelog
* Thu Feb 27 2020 Tom Hughes <tom@compton.nu> - 1.11.1-1
- Update to 1.11.1 upstream release

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed May 23 2018 Jared K. Smith <jsmith@fedoraproject.org> - 1.9.1-1
- Initial packaging
