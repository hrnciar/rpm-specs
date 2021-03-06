%{?nodejs_find_provides_and_requires}

%global packagename locate-character
%global enable_tests 1

Name:		nodejs-locate-character
Version:	2.0.5
Release:	7%{?dist}
Summary:	Get the line and column number of a specific character in a string

# license file requested at ahttps://github.com/Rich-Harris/locate-character/issues/1
License:	MIT
URL:		https://github.com/Rich-Harris/locate-character.git
Source0:	https://registry.npmjs.org/%{packagename}/-/%{packagename}-%{version}.tgz
# The test files are not included in the npm tarball.
# Source{1-9} are generated by running Source10, which pulls from the upstream
# version control repository.
Source1:	src-%{version}.tar.bz2
Source2:	tests-%{version}.tar.bz2
Source10:	dl-tests.sh

# typescript config
Source11:	https://raw.githubusercontent.com/Rich-Harris/locate-character/master/tsconfig.json
Source12:	https://raw.githubusercontent.com/Rich-Harris/locate-character/master/types.d.ts


BuildArch:	noarch
ExclusiveArch: %{nodejs_arches} noarch

BuildRequires:	nodejs-packaging
BuildRequires:	npm(typescript)

%if 0%{?enable_tests}
BuildRequires:	mocha
%endif

%description
Get the line and column number of a specific character in a string


%prep
%autosetup -n package
# setup the src and tests
%autosetup -T -D -a 1 -n package
%autosetup -T -D -a 2 -n package
cp -p %{SOURCE11} .
cp -p %{SOURCE12} .


%build
# nothing to do
tsc

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{packagename}
cp -pr package.json dist/ \
	%{buildroot}%{nodejs_sitelib}/%{packagename}

%nodejs_symlink_deps

%check
%nodejs_symlink_deps --check
%{__nodejs} -e 'require("./")'
%if 0%{?enable_tests}
NODE_ENV=test %{_bindir}/mocha -R spec
%else
%{_bindir}/echo -e "\e[101m -=#=- Tests disabled -=#=- \e[0m"
%endif

%files
%doc *.md
%{nodejs_sitelib}/%{packagename}

%changelog
* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.5-7
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed May 30 2018 Jared K. Smith <jsmith@fedoraproject.org> - 2.0.5-1
- Initial packaging
