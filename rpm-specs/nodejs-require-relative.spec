%{?nodejs_find_provides_and_requires}

%global packagename require-relative
%global enable_tests 1

Name:		nodejs-require-relative
Version:	0.8.7
Release:	5%{?dist}
Summary:	Require and resolve modules relative to a path of your choice


# license file requested upstream at https://github.com/kamicane/require-relative/issues/3
License:	MIT
URL:		https://github.com/kamicane/require-relative.git
Source0:	https://registry.npmjs.org/%{packagename}/-/%{packagename}-%{version}.tgz


BuildArch:	noarch
ExclusiveArch: %{nodejs_arches} noarch

BuildRequires:	nodejs-packaging

%if 0%{?enable_tests}
BuildRequires:	mocha
%endif

%description
Require and resolve modules relative to a path of your choice


%prep
%autosetup -n package


%build
# nothing to do

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{packagename}
cp -pr package.json *.js \
	%{buildroot}%{nodejs_sitelib}/%{packagename}

%nodejs_symlink_deps

%check
%nodejs_symlink_deps --check
%{__nodejs} -e 'require("./")'
%if 0%{?enable_tests}
%{_bindir}/echo -e "\e[103m -=#=- This package has no tests -=#=- \e[0m"
%else
%{_bindir}/echo -e "\e[101m -=#=- Tests disabled -=#=- \e[0m"
%endif

%files
%doc *.md
%{nodejs_sitelib}/%{packagename}

%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.7-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed May 30 2018 Jared K. Smith <jsmith@fedoraproject.org> - 0.8.7-1
- Initial packaging
