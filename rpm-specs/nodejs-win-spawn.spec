%{?nodejs_find_provides_and_requires}

%global packagename win-spawn
%global enable_tests 1
# there are no tests :-(

Name:		nodejs-win-spawn
Version:	2.0.0
Release:	8%{?dist}
Summary:	Spawn for node.js but in a way that works regardless of which OS you're using

# package.json lists the license as 3-clause BSD, but the source repo has no license file
# File requested at https://github.com/ForbesLindesay/win-spawn/issues/15
License:	BSD
URL:		https://github.com/ForbesLindesay/win-spawn.git
Source0:	https://registry.npmjs.org/%{packagename}/-/%{packagename}-%{version}.tgz

ExclusiveArch:	%{nodejs_arches} noarch
BuildArch:	noarch

BuildRequires:	nodejs-packaging
%if 0%{?enable_tests}
#BuildRequires:
%endif

Requires:	nodejs

%description
Spawn for node.js but in a way that works regardless of which OS you're using


%prep
%setup -q -n package



%build
# nothing to do!

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{packagename}
cp -pr package.json *.js \
	%{buildroot}%{nodejs_sitelib}/%{packagename}

mkdir -p %{buildroot}%{nodejs_sitelib}/%{packagename}/bin
install -p -D -m0755 bin/win-spawn %{buildroot}%{nodejs_sitelib}/%{packagename}/bin/win-spawn

mkdir -p %{buildroot}%{_bindir}
ln -sf %{nodejs_sitelib}/%{packagename}/bin/win-spawn \
    %{buildroot}%{_bindir}/win-spawn


%nodejs_symlink_deps

%check
%nodejs_symlink_deps --check
%{__nodejs} -e 'require("./")'
%if 0%{?enable_tests}
echo "There are no tests..."
%endif


%files
%{!?_licensedir:%global license %doc}
%doc *.md
%{nodejs_sitelib}/%{packagename}
%{_bindir}/win-spawn



%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Oct 27 2015 Jared Smith <jsmith@fedoraproject.org> - 2.0.0-1
- Initial packaging
