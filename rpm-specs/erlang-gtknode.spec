%global realname gtknode
%global upstream massemanet


Name:		erlang-%{realname}
Version:	1.0.4
Release:	10%{?dist}
Summary:	Erlang GTK2 binding
License:	MIT
URL:		https://github.com/%{upstream}/%{realname}
%if 0%{?el7}%{?fedora}
VCS:		scm:git:https://github.com/%{upstream}/%{realname}.git
%endif
Source0:	https://github.com/%{upstream}/%{realname}/archive/%{version}/%{realname}-%{version}.tar.gz
# Fedora-specific
Patch1:		erlang-gtknode-0001-Respect-CFLAGS-and-LDFLAGS.patch
# Fedora-specific
Patch2:		erlang-gtknode-0002-Clarify-port-executable-placement.patch
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	erlang-rebar
BuildRequires:	gtk2-devel
BuildRequires:	libglade2-devel
BuildRequires:	libtool


%description
Erlang GTK2 binding.


%prep
%setup -q -n %{realname}-%{version}
%patch1 -p1
%patch2 -p1


%build
%{erlang_compile}


%install
%{erlang_install}

install -D -p -m 0755 priv/generator/build/gtknode  %{buildroot}%{erlang_appdir}/priv/gtknode



%check
%{erlang_test}


%files
%license COPYING
%doc AUTHORS README.md priv/examples/
%{erlang_appdir}/


%changelog
* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.4-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.4-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.4-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Jun  6 2016 Peter Lemenkov <lemenkov@gmail.com> - 1.0.4-1
- Ver. 1.0.4

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.32-10.20110310git19ddfd5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.32-9.20110310git19ddfd5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.32-8.20110310git19ddfd5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.32-7.20110310git19ddfd5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Sep 01 2013 Peter Lemenkov <lemenkov@gmail.com> - 0.32-6.20110310git19ddfd5
- Fixed FTBFS

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.32-5.20110310git19ddfd5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.32-4.20110310git19ddfd5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.32-3.20110310git19ddfd5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jun 07 2012 Peter Lemenkov <lemenkov@gmail.com> - 0.32-2.20110310git19ddfd5
- Changed versioning scheme
- Added comment about tarball retrieving
- Fixed building with R15B

* Fri May 18 2012 Peter Lemenkov <lemenkov@gmail.com> - 0.32-1
- Ver. 0.32
