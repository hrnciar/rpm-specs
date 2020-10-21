Name:           gnushogi

%global commit 5bb0b5b2f6953b3250e965c7ecaf108215751a74
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Version:        1.5
Release:        0.12.git%{shortcommit}%{?dist}
Summary:        Shogi, the Japanese version of chess

License:        GPLv3+
URL:            https://www.gnu.org/software/gnushogi/
Source0:        https://git.savannah.gnu.org/cgit/gnushogi.git/snapshot/gnushogi-%{commit}.tar.gz

BuildRequires:  gcc
BuildRequires:  autoconf, automake, texinfo-tex, ncurses-devel

%if 0%{?fedora} >= 24
Recommends:     xboard
%endif

%if ( 0%{?rhel} <= 7 ) || ( 0%{?fedora} < 28 )
Requires(post): info
Requires(preun): info
%endif

%description
GNU shogi is a program that plays shogi, the Japanese version of chess, 
against a human (or computer) opponent. It is only the AI engine, and you 
will likely want to use a GUI front-end (XBoard, for example) to be more 
comfortable.

%prep
%setup -qn %{name}-%{commit}
./autogen.sh

%build
%configure
%if 0%{?rhel} <= 6
make %{?_smp_mflags}
%else
%make_build
%endif
make -C gnushogi gnushogi.bbk
# mini tbk is currently empty, not implemented yet
#make -C gnushogi gnuminishogi.bbk


%install
%make_install
rm -f %{buildroot}%{_infodir}/dir
cp gnushogi/gnushogi.bbk %{buildroot}%{_libdir}/%{name}


%post
# if xboard is installed, add gnushogi into xboard default engine list
if [ -f /etc/xboard.conf ] ; then
    sed -i '/-firstChessProgramNames/a "GNUShogi" -fcp gnushogi -variant shogi' /etc/xboard.conf
fi

%preun
# if xboard is installed, try remove gnushogi from the engine list
grep '\-fcp gnushogi \-variant shogi' /etc/xboard.conf > /dev/null 2>&1
if [ $? = 0 ] ; then
    sed -i '/-fcp gnushogi -variant shogi/d' /etc/xboard.conf
fi

%files
%license COPYING
%doc AUTHORS ChangeLog NEWS README TODO
%{_bindir}/gnuminishogi
%{_bindir}/gnushogi
%{_libdir}/%{name}
%{_docdir}/%{name}
%{_infodir}/%{name}.info.*
%{_mandir}/man6/%{name}.6.gz

%changelog
* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-0.12.git5bb0b5b
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-0.11.git5bb0b5b
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-0.10.git5bb0b5b
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-0.9.git5bb0b5b
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Apr 24 2019 Björn Esser <besser82@fedoraproject.org> - 1.5-0.8.git5bb0b5b
- Remove hardcoded gzip suffix from GNU info pages

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-0.7.git5bb0b5b
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-0.6.git5bb0b5b
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Jun 16 2018 Chen Chen <aflyhorse@hotmail.com> 1.5-0.5.git5bb0b5b
- Wrap install-info in if block as #packaging-committee/issue/773

* Fri Feb 9 2018 Chen Chen <aflyhorse@hotmail.com> 1.5-0.4.git5bb0b5b
- Let the package own its lib and doc directories.

* Thu Feb 8 2018 Chen Chen <aflyhorse@hotmail.com> 1.5-0.3.git5bb0b5b
- Fix syntax error and add bbk, again thanks to Ben.

* Tue Jan 23 2018 Chen Chen <aflyhorse@hotmail.com> 1.5-0.2.git5bb0b5b
- Improve the spec file, thanks to Ben Rosser <rosser.bjr@gmail.com>

* Thu Jan 4 2018 Chen Chen <aflyhorse@hotmail.com> 1.5-0.1.git5bb0b5b
- Initial version.
