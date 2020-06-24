%{?nodejs_find_provides_and_requires}

%global packagename optionator

# Set to 0 to bootstrap optionator as a dependency for LiveScript itself
%global bootstrap 1

# Tests also require LiveScript, and will need to be disabled during bootstrap
%global enable_tests 0

Name:		nodejs-optionator
Version:	0.8.1
Release:	8%{?dist}
Summary:	Option parsing and help generation

License:	MIT
URL:		https://github.com/gkz/optionator.git
Source0:	https://registry.npmjs.org/%{packagename}/-/%{packagename}-%{version}.tgz
# The test files are not included in the npm tarball.
# Source1,2 is generated by running Source10, which pulls from the upstream
# version control repository.
Source1:	tests-%{version}.tar.bz2
Source2:	src-%{version}.tar.bz2
Source10:	dl-tests.sh
# The package.json.ls file isn't in the tarball either
Source11:	https://raw.githubusercontent.com/gkz/optionator/%{version}/package.json.ls


BuildArch:	noarch
%if 0%{?fedora} >= 19
ExclusiveArch: %{nodejs_arches} noarch
%else
ExclusiveArch: %{ix86} x86_64 %{arm} noarch
%endif

BuildRequires:	nodejs-packaging
BuildRequires:	npm(deep-is)
BuildRequires:	npm(fast-levenshtein)
BuildRequires:	npm(levn)
BuildRequires:	npm(prelude-ls)
BuildRequires:	npm(type-check)
BuildRequires:	npm(wordwrap)
%if 0%{?enable_tests}
BuildRequires:	mocha
%endif
%if !0%{?bootstrap}
BuildRequires:	npm(LiveScript)
%endif

%description
Option parsing and help generation


%prep
%setup -q -n package
# setup the tests
%setup -q -T -D -a 1 -n package
# setup the source files
%setup -q -T -D -a 2 -n package
# copy package.json.ls
cp -p %{SOURCE11} .



%build
%if !0%{?bootstrap}
%{_bindir}/echo -e "\e[102m -=#=- Building from source -=#=- \e[0m"
# Build from source
#
# Clear the lib/ directory
rm -rf ./lib/
mkdir ./lib/
# Next, build package.json from package.json.ls
%{_bindir}/lsc --compile package.json.ls
# Next, compile the the lib/ directory from the src/ directory
%{_bindir}/lsc --output lib --bare --compile src/*.ls
# Last but not least, clean up behind ourselves and erase the node_modules/ directory
rm -rf ./node_modules/
%endif


%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{packagename}
cp -pr package.json lib/ \
	%{buildroot}%{nodejs_sitelib}/%{packagename}

%nodejs_symlink_deps

%check
%nodejs_symlink_deps --check
%{__nodejs} -e 'require("./")'
%if 0%{?enable_tests}
%{_bindir}/mocha -R dot --ui tdd --compilers ls:LiveScript
%else
%{_bindir}/echo -e "\e[101m -=#=- Tests disabled -=#=- \e[0m"
%endif


%files
%{!?_licensedir:%global license %doc}
%doc *.md
%license LICENSE
%{nodejs_sitelib}/%{packagename}


%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Feb 16 2016 Jared Smith <jsmith@fedoraproject.org> - 0.8.1-1
- Initial packaging