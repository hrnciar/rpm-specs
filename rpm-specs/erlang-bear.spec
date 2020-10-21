%global realname bear
%global upstream folsom-project


Name:		erlang-%{realname}
Version:	0.8.7
Release:	6%{?dist}
BuildArch:	noarch
Summary:	A set of statistics functions for erlang
License:	ASL 2.0
URL:		https://github.com/%{upstream}/%{realname}
VCS:		scm:git:https://github.com/%{upstream}/%{realname}.git
Source0:	https://github.com/%{upstream}/%{realname}/archive/%{version}/%{realname}-%{version}.tar.gz
Patch1:		erlang-bear-0001-Compile-w-o-export_all.patch
BuildRequires:	erlang-rebar


%description
A set of statistics functions for Erlang. Currently bear is focused on use
inside the Folsom Erlang metrics library but all of these functions are generic
and useful in other situations.


%prep
%autosetup -p1 -n %{realname}-%{version}


%build
%{erlang_compile}


%install
%{erlang_install}


%check
%{erlang_test}


%files
%license LICENSE
%doc README.md
%{erlang_appdir}/


%changelog
* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.7-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.7-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Nov 11 2019 Peter Lemenkov <lemenkov@gmail.com> - 0.8.7-4
- Rebuilt with fixed Rebar

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Sep 19 2018 Peter Lemenkov <lemenkov@gmail.com> - 0.8.7-1
- Ver. 0.8.7

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Apr 27 2016 Peter Lemenkov <lemenkov@gmail.com> - 0.8.2-3
- More spec-file cleanups

* Mon Mar  7 2016 Peter Lemenkov <lemenkov@gmail.com> - 0.8.2-2
- Spec-file cleanups

* Fri Feb 12 2016 Peter Lemenkov <lemenkov@gmail.com> - 0.8.2-1
- Ver. 0.8.2 (Backwards API/ABI compatible release)

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sun Mar 03 2013 Peter Lemenkov <lemenkov@gmail.com> - 0.1.3-1
- Ver. 0.1.3 (Backwards API/ABI compatible release)

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Dec 21 2012 Peter Lemenkov <lemenkov@gmail.com> - 0.1.2-1
- Ver. 0.1.2 (API/ABI compatible bugfix release)

* Sun Sep 02 2012 Peter Lemenkov <lemenkov@gmail.com> - 0.1.1-1
- Initial build
