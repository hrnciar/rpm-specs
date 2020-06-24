%{?nodejs_find_provides_and_requires}

%global packagename tap-out
%global enable_tests 1

Name:		nodejs-tap-out
Version:	2.0.0
Release:	6%{?dist}
Summary:	A different tap parser

License:	MIT
URL:		https://github.com/scottcorgan/tap-out
Source0:	https://registry.npmjs.org/%{packagename}/-/%{packagename}-%{version}.tgz

BuildArch:	noarch
%if 0%{?fedora} >= 19
ExclusiveArch: %{nodejs_arches} noarch
%else
ExclusiveArch: %{ix86} x86_64 %{arm} noarch
%endif

BuildRequires:	nodejs-packaging
BuildRequires:	npm(readable-stream)
BuildRequires:	npm(re-emitter)
BuildRequires:	npm(split)
BuildRequires:	npm(trim)
%if 0%{?enable_tests}
BuildRequires:	npm(tape)
%endif

%description
A different tap parser


%prep
%setup -q -n package

%nodejs_fixdep readable-stream


%build
# nothing to do!

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{packagename}
cp -pr package.json index.js lib/ \
	%{buildroot}%{nodejs_sitelib}/%{packagename}

mkdir -p %{buildroot}%{nodejs_sitelib}/%{packagename}/bin
install -p -D -m0755 bin/cmd.js %{buildroot}%{nodejs_sitelib}/%{packagename}/bin/cmd.js

mkdir -p %{buildroot}%{_bindir}
ln -sf %{nodejs_sitelib}/%{packagename}/bin/cmd.js \
    %{buildroot}%{_bindir}/%{packagename}

%nodejs_symlink_deps

%check
%nodejs_symlink_deps --check
%{__nodejs} -e 'require("./")'
%if 0%{?enable_tests}
# insert test suite here
%{_bindir}/tape test/index.js
%else
%{_bindir}/echo -e "\e[101m -=#=- Tests disabled -=#=- \e[0m"
%endif


%files
%{!?_licensedir:%global license %doc}
%doc *.md
%license LICENSE
%{nodejs_sitelib}/%{packagename}
%{_bindir}/tap-out


%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Sep 19 2017 Jared Smith <jsmith@fedoraproject.org> - 2.0.0-1
- Update to upstream 2.0.0 release

* Wed Apr 19 2017 Jared Smith <jsmith@fedoraproject.org> - 1.4.2-1
- Update to upstream 1.4.2 release

* Tue Feb 23 2016 Jared Smith <jsmith@fedoraproject.org> - 1.4.1-1
- Initial packaging
