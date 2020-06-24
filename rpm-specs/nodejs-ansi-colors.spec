%{?nodejs_find_provides_and_requires}

%global packagename ansi-colors
%global enable_tests 1

Name:		nodejs-ansi-colors
Version:	0.2.0
Release:	6%{?dist}
Summary:	Collection of ansi colors and styles

License:	MIT
URL:		https://github.com/doowb/ansi-colors
Source0:	https://registry.npmjs.org/%{packagename}/-/%{packagename}-%{version}.tgz
# The test files are not included in the npm tarball.
Source1:	https://raw.githubusercontent.com/doowb/ansi-colors/master/test.js


ExclusiveArch:	%{nodejs_arches} noarch
BuildArch:	noarch

BuildRequires:	nodejs-packaging
BuildRequires:	npm(lazy-cache)
%if 0%{?enable_tests}
BuildRequires:	mocha
BuildRequires:	npm(ansi-bgblack)
BuildRequires:	npm(ansi-bgblue)
BuildRequires:	npm(ansi-bgcyan)
BuildRequires:	npm(ansi-bggreen)
BuildRequires:	npm(ansi-bgmagenta)
BuildRequires:	npm(ansi-bgred)
BuildRequires:	npm(ansi-bgwhite)
BuildRequires:	npm(ansi-bgyellow)
BuildRequires:	npm(ansi-black)
BuildRequires:	npm(ansi-blue)
BuildRequires:	npm(ansi-bold)
BuildRequires:	npm(ansi-cyan)
BuildRequires:	npm(ansi-dim)
BuildRequires:	npm(ansi-gray)
BuildRequires:	npm(ansi-green)
BuildRequires:	npm(ansi-grey)
BuildRequires:	npm(ansi-hidden)
BuildRequires:	npm(ansi-inverse)
BuildRequires:	npm(ansi-italic)
BuildRequires:	npm(ansi-magenta)
BuildRequires:	npm(ansi-red)
BuildRequires:	npm(ansi-reset)
BuildRequires:	npm(ansi-strikethrough)
BuildRequires:	npm(ansi-underline)
BuildRequires:	npm(ansi-white)
BuildRequires:	npm(ansi-yellow)
%endif

%description
Collection of ansi colors and styles.


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
%{_bindir}/mocha -R spec
%else
%{_bindir}/echo -e "\e[101m -=#=- Tests disabled -=#=- \e[0m"
%endif

%files
%doc README.md
%license LICENSE
%{nodejs_sitelib}/%{packagename}

%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Apr 14 2017 Jared Smith <jsmith@fedoraproject.org> - 0.2.0-1
- Initial packaging