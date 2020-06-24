%{?nodejs_find_provides_and_requires}

%global packagename esrecurse
%global enable_tests 1

Name:		nodejs-esrecurse
Version:	4.1.0
Release:	9%{?dist}
Summary:	ECMAScript AST recursive visitor

License:	BSD
URL:		https://github.com/estools/esrecurse.git
Source0:	https://registry.npmjs.org/%{packagename}/-/%{packagename}-%{version}.tgz
# The test files are not included in the npm tarball.
# Source1 is generated by running Source10, which pulls from the upstream
# version control repository.
Source1:	tests-%{version}.tar.bz2
Source10:	dl-tests.sh
# Grab the README.md file, as it contains the license as well
Source11:	https://raw.githubusercontent.com/estools/esrecurse/%{version}/README.md


BuildArch:	noarch
%if 0%{?fedora} >= 19
ExclusiveArch: %{nodejs_arches} noarch
%else
ExclusiveArch: %{ix86} x86_64 %{arm} noarch
%endif

BuildRequires:	nodejs-packaging
BuildRequires:	npm(estraverse)
BuildRequires:	npm(object-assign)
%if 0%{?enable_tests}
BuildRequires:	coffee-script
BuildRequires:	mocha
BuildRequires:	npm(chai)
%endif

%description
ECMAScript AST recursive visitor


%prep
%setup -q -n package
# setup the tests
%setup -q -T -D -a 1 -n package
# copy the README.md file
cp -p %{SOURCE11} .
# Extract the license from the README.md file
sed '0,/### License/d' README.md > LICENSE.md

%nodejs_fixdep estraverse

%build
# nothing to do!

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{packagename}
cp -pr package.json esrecurse.js \
	%{buildroot}%{nodejs_sitelib}/%{packagename}

%nodejs_symlink_deps

%check
%nodejs_symlink_deps --check
%{__nodejs} -e 'require("./")'
%if 0%{?enable_tests}
%{_bindir}/mocha -R spec --compilers coffee:coffee-script/register
%else
%{_bindir}/echo -e "\e[101m -=#=- Tests disabled -=#=- \e[0m"
%endif


%files
%{!?_licensedir:%global license %doc}
%doc README.md
%license LICENSE.md
%{nodejs_sitelib}/%{packagename}


%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Aug 05 2016 Jared Smith <jsmith@fedoraproject.org> - 4.1.0-2
- Make building the license file more robust

* Thu Jul 14 2016 Jared Smith <jsmith@fedoraproject.org> - 4.1.0-1
- Update to upstream 4.1.0 release

* Wed Feb 17 2016 Jared Smith <jsmith@fedoraproject.org> - 4.0.0-1
- Initial packaging