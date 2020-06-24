%{?nodejs_find_provides_and_requires}

%global packagename arr-diff
%global enable_tests 1

Name:		nodejs-arr-diff
Version:	4.0.0
Release:	6%{?dist}
Summary:	Returns an array with only the unique values from the first array

License:	MIT
URL:		https://github.com/jonschlinkert/arr-diff.git
Source0:	https://registry.npmjs.org/%{packagename}/-/%{packagename}-%{version}.tgz
# The test files are not included in the npm tarball
Source1:	https://raw.githubusercontent.com/jonschlinkert/arr-diff/%{version}/test.js


BuildArch:	noarch
%if 0%{?fedora} >= 19
ExclusiveArch: %{nodejs_arches} noarch
%else
ExclusiveArch: %{ix86} x86_64 %{arm} noarch
%endif

BuildRequires:	nodejs-packaging
BuildRequires:	npm(arr-flatten)
%if 0%{?enable_tests}
BuildRequires:	mocha
BuildRequires:	npm(should)
%endif

%description
Returns an array with only the unique values from the first array, by excluding
all values from additional arrays using strict equality for comparisons.


%prep
%setup -q -n package
# setup the tests
cp -p %{SOURCE1} .

chmod -x ./LICENSE


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
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Sep 23 2017 Jared Smith <jsmith@fedoraproject.org> - 4.0.0-1
- Update to upstream 4.0.0 release

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 12 2016 Jared Smith <jsmith@fedoraproject.org> - 2.0.0-2
- Fix BuildRequires and exclude test.js from package

* Wed Feb  3 2016 Jared Smith <jsmith@fedoraproject.org> - 2.0.0-1
- Initial packaging
