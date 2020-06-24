%global realname fuse
%global upstream jlouis


Name:		erlang-%{realname}
Version:	2.4.2
Release:	4%{?dist}
BuildArch:	noarch
Summary:	A Circuit Breaker for Erlang
License:	MIT
URL:		https://github.com/%{upstream}/%{realname}
VCS:		scm:git:https://github.com/%{upstream}/%{realname}.git
Source0:	https://github.com/%{upstream}/%{realname}/archive/%{version}/%{realname}-%{version}.tar.gz
Patch1:		erlang-fuse-0001-Disable-support-for-Prometheus-in-Fedora.patch
BuildRequires:	erlang-exometer_core
BuildRequires:	erlang-folsom
# FIXME include into fedora oneday - see patch no. 1
#BuildRequires:	erlang-prometheus
BuildRequires:	erlang-rebar


%description
This application implements a so-called circuit-breaker for Erlang.


%prep
%autosetup -p1 -n %{realname}-%{version}


%build
%{erlang_compile}


%install
%{erlang_install}


%check
# Requires a proprietary eqc library
#%%{erlang_test}


%files
%license LICENSE
%doc README.md
%{erlang_appdir}/


%changelog
* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Oct 02 2018 Peter Lemenkov <lemenkov@gmail.com> - 2.4.2-1
- Ver. 2.4.2
- Switch to noarch

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 31 2017 Peter Lemenkov <lemenkov@gmail.com> - 2.4.0-1
- Initial build

