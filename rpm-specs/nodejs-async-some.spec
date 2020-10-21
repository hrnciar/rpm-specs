# spec file for package nodejs-nodejs-async-some

%global npm_name async-some
%{?nodejs_find_provides_and_requires}

# Disable tests since tap is not installable/missing
%bcond_with tests

Name:		nodejs-async-some
Version:	1.0.2
Release:	12%{?dist}
Summary:	Short-circuited, asynchronous version of Array.prototype.some
Url:		https://github.com/othiym23/async-some
Source0:	https://registry.npmjs.org/%{npm_name}/-/%{npm_name}-%{version}.tgz
License:	ISC

BuildArch:	noarch
ExclusiveArch:	%{nodejs_arches} noarch

BuildRequires:	nodejs-devel
BuildRequires:	nodejs-packaging

%if %{with tests}
BuildRequires:	npm(dezalgo)
BuildRequires:	npm(tap)
%endif

%description
Short-circuited, asynchronous version of Array.prototype.some

%prep
%setup -q -n package

%build
#nothing to do

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{npm_name}

cp -pr package.json some.js \
	%{buildroot}%{nodejs_sitelib}/%{npm_name}

%{nodejs_symlink_deps}

%check
%{nodejs_symlink_deps} --check
%if %{with tests}
tap test/*.js
%endif

%files
%{nodejs_sitelib}/async-some

%doc README.md
%license LICENSE

%changelog
* Wed Aug 12 2020 Jan Staněk <jstanek@redhat.com> - 1.0.2-12
- Disable tests as the tap dependency is not installable

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-11
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 24 2015 Zuzana Svetlikova <zsvetlik@redhat.com> - 1.0.2-1
- Updated to new upstream release

* Wed May 13 2015 Zuzana Svetlikova <zsvetlik@redhat.com> - 1.0.1-1
- Initial build
