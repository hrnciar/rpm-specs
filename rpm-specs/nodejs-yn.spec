%{?nodejs_find_provides_and_requires}

%global packagename yn

# Tests require npm(ava), which is not yet in Fedora
%global enable_tests 0

Name:		nodejs-yn
Version:	2.0.0
Release:	7%{?dist}
Summary:	Parse yes/no like values

License:	MIT
URL:		https://github.com/sindresorhus/yn.git
Source0:	https://registry.npmjs.org/%{packagename}/-/%{packagename}-%{version}.tgz
# version control repository.
Source1:	https://raw.githubusercontent.com/sindresorhus/yn/v%{version}/test.js


BuildArch:	noarch
ExclusiveArch: %{nodejs_arches} noarch

BuildRequires:	nodejs-packaging

%if 0%{?enable_tests}
BuildRequires:	ava
%endif

%description
Parse yes/no like values


%prep
%autosetup -n package
# setup the tests
cp -p %{SOURCE1} .


%build
# nothing to do

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{packagename}
cp -pr package.json index.js lenient.js \
	%{buildroot}%{nodejs_sitelib}/%{packagename}

%nodejs_symlink_deps

%check
%nodejs_symlink_deps --check
%{__nodejs} -e 'require("./")'
%if 0%{?enable_tests}
%{_bindir}/ava -v
%else
%{_bindir}/echo -e "\e[101m -=#=- Tests disabled -=#=- \e[0m"
%endif

%files
%doc *.md
%license license
%{nodejs_sitelib}/%{packagename}

%changelog
* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-7
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed May 23 2018 Jared K. Smith <jsmith@fedoraproject.org> - 2.0.0-1
- Initial packaging
