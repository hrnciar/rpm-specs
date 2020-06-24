%global realname stdlib2
%global upstream kivra
%global git_tag 4cf3a7032347762c5f077b93dd4f6a2ce994c78d
%global short_tag %(c=%{git_tag}; echo ${c:0:7})


Name:		erlang-%{realname}
Version:	0
Release:	0.8.20180928git%{short_tag}%{?dist}
BuildArch:	noarch
Summary:	Erlang stdlib extensions
License:	BSD
URL:		https://github.com/%{upstream}/%{realname}
VCS:		scm:git:https://github.com/%{upstream}/%{realname}.git
#Source0:	https://github.com/%{upstream}/%{realname}/archive/%{version}/%{realname}-%{version}.tar.gz
Source0:	https://github.com/%{upstream}/%{realname}/archive/%{git_tag}/%{realname}-%{version}.tar.gz
Patch1:		erlang-stdlib2-0001-Add-missing-f2l-and-l2f-macros.patch
Patch2:		erlang-stdlib2-0002-Ensure-timestamps-are-monotonically-increasing.patch
Patch3:		erlang-stdlib2-0003-Properly-test-for-alive-process.patch
BuildRequires:	erlang-folsom
BuildRequires:	erlang-rebar


%description
Erlang stdlib extensions.


%prep
%autosetup -p1 -n %{realname}-%{git_tag}


%build
%{erlang_compile}


%install
%{erlang_install}


%check
%{erlang_test}


%files
%doc README.md
%{erlang_appdir}/


%changelog
* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.8.20180928git4cf3a70
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.7.20180928git4cf3a70
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.6.20180928git4cf3a70
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Oct 02 2018 Peter Lemenkov <lemenkov@gmail.com> - 0-0.5.20180928git4cf3a70
- New git snapshot
- Convert to noarch

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.4.20170810git5ccd9b2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Mar 21 2018 Peter Lemenkov <lemenkov@gmail.com> - 0-0.3.20170810git5ccd9b2
- Rebuild for Erlang 20 (with proper builddeps)

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.2.20170810git5ccd9b2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Aug 22 2017 Peter Lemenkov <lemenkov@gmail.com> - 0-0.1.20170810git5ccd9b2
- Initial build
