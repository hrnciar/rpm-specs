%{?nodejs_find_provides_and_requires}

%global packagename use
%global enable_tests 1

Name:		nodejs-use
Version:	3.0.0
Release:	10%{?dist}
Summary:	Easily add plugin support to your node.js application

License:	MIT
URL:		https://github.com/jonschlinkert/use
Source0:	https://registry.npmjs.org/%{packagename}/-/%{packagename}-%{version}.tgz
# The example files are not included in the npm tarball.
# Source1 is generated by running Source10, which pulls from the upstream
# version control repository.
Source1:	examples-%{version}.tar.bz2
Source10:	dl-tests.sh
# tests aren't in npm tarball either, so grab from GitHub
Source11:	https://raw.githubusercontent.com/jonschlinkert/use/%{version}/test.js


ExclusiveArch:	%{nodejs_arches} noarch
BuildArch:	noarch

BuildRequires:	nodejs-packaging
%if 0%{?enable_tests}
BuildRequires:	mocha
BuildRequires:	npm(define-property)
BuildRequires:	npm(extend-shallow)
BuildRequires:	npm(isobject)
%endif

%description
Easily add plugin support to your node.js application.


%prep
%autosetup -n package
# setup the examples
%autosetup -T -D -a 1 -n package
# setup the tests
cp -p %{SOURCE11} .

# allow older version of npm(isobject)
%nodejs_fixdep isobject
# allow newer version of npm(define-property)
%nodejs_fixdep define-property

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
%doc README.md examples/
%license LICENSE
%{nodejs_sitelib}/%{packagename}

%changelog
* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-10
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Aug 18 2017 Jared Smith <jsmith@fedoraproject.org> - 3.0.0-3
- Relax dependency on npm(define-property)

* Fri Apr 14 2017 Jared Smith <jsmith@fedoraproject.org> - 3.0.0-2
- Relax dependency on npm(isobject)

* Fri Apr 14 2017 Jared Smith <jsmith@fedoraproject.org> - 3.0.0-1
- Initial packaging
