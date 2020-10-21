%{?nodejs_find_provides_and_requires}

%global packagename extglob

# tests disabled due to circular dependency on micromatch
%global enable_tests 0

Name:		nodejs-extglob
Version:	2.0.4
Release:	8%{?dist}
Summary:	Convert extended globs to regex-compatible strings

License:	MIT
URL:		https://github.com/jonschlinkert/extglob.git
Source0:	https://registry.npmjs.org/%{packagename}/-/%{packagename}-%{version}.tgz
# The test files are not included in the npm tarball.
# Source1 is generated by running Source10, which pulls from the upstream
# version control repository.
Source1:	tests-%{version}.tar.bz2
Source2:	examples-%{version}.tar.bz2
Source10:	dl-tests.sh

Patch0:		nodejs-extglob_use-newer-snapdragon.patch

BuildArch:	noarch
%if 0%{?fedora} >= 19
ExclusiveArch: %{nodejs_arches} noarch
%else
ExclusiveArch: %{ix86} x86_64 %{arm} noarch
%endif

BuildRequires:	nodejs-packaging
BuildRequires:	npm(ansi-green)
BuildRequires:	npm(array-unique)
BuildRequires:	npm(expand-brackets)
BuildRequires:	npm(extend-shallow)
BuildRequires:	npm(fragment-cache)
BuildRequires:	npm(is-extglob)
BuildRequires:	npm(snapdragon)
BuildRequires:	npm(success-symbol)
BuildRequires:	npm(to-regex)
%if 0%{?enable_tests}
BuildRequires:	mocha
BuildRequires:	npm(bash-match)
BuildRequires:	npm(micromatch)
%endif

%description
Convert extended globs to regex-compatible strings. Add (almost) the expressive
power of regular expressions to glob patterns.


%prep
%setup -q -n package
# setup the tests
%setup -q -T -D -a 1 -n package
%setup -q -T -D -a 2 -n package

%patch0 -p1

rm lib/.DS_Store

%nodejs_fixdep expand-brackets '~3.0.0'
%nodejs_fixdep snapdragon '~0.12.0'
%nodejs_fixdep define-property

%build
# nothing to do!

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{packagename}
cp -pr package.json index.js lib/ \
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
%doc *.md examples/
%license LICENSE
%{nodejs_sitelib}/%{packagename}


%changelog
* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.4-8
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Apr 20 2018 Jared K. Smith <jsmith@fedoraproject.org> - 2.0.4-2
- Use newer npm(snapdragon)

* Wed Apr 18 2018 Jared K. Smith <jsmith@fedoraproject.org> - 2.0.4-1
- Update to upstream 2.0.4 release

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Sep 19 2017 Jared Smith <jsmith@fedoraproject.org> - 2.0.2-1
- Update to upstream 2.0.2 release

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Feb  9 2016 Jared Smith <jsmith@fedoraproject.org> - 0.3.2-1
- Initial packaging
