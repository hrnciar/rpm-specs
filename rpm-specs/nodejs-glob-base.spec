%{?nodejs_find_provides_and_requires}

%global packagename glob-base

# disabled due to failing tests
%global enable_tests 0

Name:		nodejs-glob-base
Version:	0.3.0
Release:	11%{?dist}
Summary:	Returns an object with the (non-glob) base path and the actual pattern

License:	MIT
URL:		https://github.com/jonschlinkert/glob-base.git
Source0:	https://registry.npmjs.org/%{packagename}/-/%{packagename}-%{version}.tgz
# The test files are not included in the npm tarball.
Source1:	https://raw.githubusercontent.com/jonschlinkert/glob-base/%{version}/test.js


BuildArch:	noarch
%if 0%{?fedora} >= 19
ExclusiveArch: %{nodejs_arches} noarch
%else
ExclusiveArch: %{ix86} x86_64 %{arm} noarch
%endif

BuildRequires:	nodejs-packaging
BuildRequires:	npm(glob-parent)
BuildRequires:	npm(is-glob)
%if 0%{?enable_tests}
BuildRequires:	mocha
BuildRequires:	npm(should)
%endif

%description
Returns an object with the (non-glob) base path and the actual pattern.


%prep
%setup -q -n package
# setup the tests
cp -p %{SOURCE1} .

%nodejs_fixdep glob-parent
%nodejs_fixdep is-glob


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
%{_bindir}/echo "Tests disabled..."
%endif


%files
%{!?_licensedir:%global license %doc}
%doc *.md
%license LICENSE
%{nodejs_sitelib}/%{packagename}


%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Sep 22 2017 Jared Smith <jsmith@fedoraproject.org> - 0.3.0-6
- Relax dependency on npm(is-glob)

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Jared Smith <jsmith@fedoraproject.org> - 0.3.0-3
- Turn on build-time checks
- Relax dependency on npm(glob-parent)

* Tue Jul 19 2016 Jared Smith <jsmith@fedoraproject.org> - 0.3.0-2
- Add npm(should) to BuildRequires

* Tue Feb  9 2016 Jared Smith <jsmith@fedoraproject.org> - 0.3.0-1
- Initial packaging
