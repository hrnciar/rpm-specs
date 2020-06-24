%global realname riak_control
%global upstream basho


Name:		erlang-%{realname}
Version:	2.1.7
Release:	7%{?dist}
BuildArch:	noarch
Summary:	Admin UI for Riak
License:	ASL 2.0
URL:		https://github.com/%{upstream}/%{realname}
%if 0%{?el7}%{?fedora}
VCS:		scm:git:https://github.com/%{upstream}/%{realname}.git
%endif
Source0:	https://github.com/%{upstream}/%{realname}/archive/%{version}/%{realname}-%{version}.tar.gz
Patch1:		erlang-riak_control-0001-Don-t-use-deprecated-functions.patch
# https://github.com/basho/riak_control/pull/201
Patch2:		erlang-riak_control-0002-Do-not-warn-about-export_all.patch
BuildRequires:	erlang-erlydtl
BuildRequires:	erlang-rebar
BuildRequires:	erlang-riak_core
BuildRequires:	erlang-webmachine


%description
Riak Control is a set of webmachine resources, all accessible via the
/admin/* paths, allow you to inspect your running cluster, and manipulate
it in various ways.


%prep
%autosetup -p1 -n %{realname}-%{version}
chmod 644 priv/admin/fonts/*


%build
%{erlang_compile}


%install
%{erlang_install}

cp -arv priv/ templates/ %{buildroot}%{erlang_appdir}/


%check
# Some tests requires a proprietary library - QuickCheck
%{erlang_test}


%files
%license LICENSE
%doc README.md
%{erlang_appdir}/


%changelog
* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.7-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.7-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.7-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Jun 13 2018 Randy Barlow <bowlofeggs@fedoraproject.org> - 2.1.7-3
- Convert into a noarch package.
- Rebuild against the noarch lager (#1589611).
- Fix a FTBFS against OTP/20.

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Aug 21 2017 Peter Lemenkov <lemenkov@gmail.com> - 2.1.7-1
- Ver. 2.1.7

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Apr 22 2016 Peter Lemenkov <lemenkov@gmail.com> - 2.1.2-1
- Ver. 2.1.2

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org>
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Aug 01 2013 Peter Lemenkov <lemenkov@gmail.com> - 1.3.2-3
- Actually fix version mismatch

* Wed Jul 31 2013 Peter Lemenkov <lemenkov@gmail.com> - 1.3.2-2
- Fix version mismatch

* Wed Jul 03 2013 Peter Lemenkov <lemenkov@gmail.com> - 1.3.2-1
- Ver. 1.3.2

* Sun Mar 24 2013 Peter Lemenkov <lemenkov@gmail.com> - 1.3.1-1
- Ver. 1.3.1

* Tue Mar 12 2013 Peter Lemenkov <lemenkov@gmail.com> - 1.3.0-1
- Ver. 1.3.0

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sun Nov 18 2012 Peter Lemenkov <lemenkov@gmail.com> - 1.2.1-2
- Fixed HTTPS-only access

* Fri Oct 19 2012 Peter Lemenkov <lemenkov@gmail.com> - 1.2.1-1
- Ver. 1.2.1

* Thu Jul 26 2012 Peter Lemenkov <lemenkov@gmail.com> - 0.1.2-2
- Fixed mixed macro usage in spec (mostly cosmetic change)
- Dropped remaining stuff required by EL5

* Thu May 17 2012 Peter Lemenkov <lemenkov@gmail.com> - 0.1.2-1
- Initial package
