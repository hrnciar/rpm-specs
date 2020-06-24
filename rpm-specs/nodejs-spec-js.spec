%{?nodejs_find_provides_and_requires}

%global packagename spec-js
%global enable_tests 1

Name:		nodejs-spec-js
Version:	1.0.0
Release:	5%{?dist}
Summary:	Creates fast, prototypicaly inherited, super-calling constructors

License:	MIT
URL:		https://github.com/KoryNunn/spec.git
Source0:	https://registry.npmjs.org/%{packagename}/-/%{packagename}-%{version}.tgz
Source1:	https://raw.githubusercontent.com/KoryNunn/spec/master/test/test.js
Source2:	https://raw.githubusercontent.com/KoryNunn/spec/master/LICENSE.txt

BuildArch:	noarch
ExclusiveArch: %{nodejs_arches} noarch

BuildRequires:	nodejs-packaging

%if 0%{?enable_tests}
BuildRequires:	npm(tape)
%endif

%description
Creates fast, prototypicaly inherited, super-calling constructors


%prep
%autosetup -n package
# setup the tests
mkdir test
cp -p %{SOURCE1} test/
# the license
cp -p %{SOURCE2} .

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
%__nodejs test/test.js
%else
%{_bindir}/echo -e "\e[101m -=#=- Tests disabled -=#=- \e[0m"
%endif

%files
%doc *.md
%license LICENSE.txt
%{nodejs_sitelib}/%{packagename}

%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon May 21 2018 Jared K. Smith <jsmith@fedoraproject.org> - 1.0.0-1
- Initial packaging
