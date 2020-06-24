Name: esorex
Version: 3.13.2
Release: 3%{?dist}
Summary: Recipe Execution Tool of the European Southern Observatory 

License: GPLv2+
URL: http://www.eso.org/observing/cpl/esorex.html
Source0: ftp://ftp.eso.org/pub/dfs/pipelines/libraries/%{name}/%{name}-%{version}.tar.gz

BuildRequires: gcc gcc-c++
BuildRequires: cpl-devel
BuildRequires: cfitsio-devel

%description
EsoRex is the ESO Recipe Execution Tool. It can list, configure and 
execute CPL-based recipes from the command line.
One of the features provided by the CPL is the ability to create 
data-reduction algorithms that run as plugins (dynamic libraries). These 
are called recipes and are one of the main aspects of the 
CPL data-reduction development environment.

%prep
%setup -q

%build
%configure  --with-cpl-libs=%{_libdir}
make %{?_smp_mflags}

%install
make DESTDIR=%{buildroot} install

%files
%doc AUTHORS README BUGS ChangeLog
%license COPYING
%config(noreplace) %{_sysconfdir}/*
%{_bindir}/*
%{_datadir}/bash-completion/completions/esorex

%changelog
* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.13.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.13.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Feb 25 2019 Sergio Pascual <sergiopr@fedoraproject.org> - 3.13.2-1
- New upstream version (3.13.2)

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.13.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Oct 06 2018 Sergio Pascual <sergiopr@fedoraproject.org> - 3.13.1-1
- New upstream version (3.13.1)

* Tue Jul 17 2018 Christian Dersch <lupinix@fedoraproject.org> - 3.12.3-8
- BuildRequires: gcc-c++

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.12.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 23 2018 Christian Dersch <lupinix@mailbox.org> - 3.12.3-6
- rebuilt for cfitsio 3.420 (so version bump)

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.12.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.12.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.12.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.12.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Apr 21 2016 Sergio Pascual <sergiopr@fedoraproject.org> - 3.12.3-1
- New upstream version (3.12.3)

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.10.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.10.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.10.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Mon Jun 16 2014 Sergio Pascual <sergiopr@fedoraproject.org> - 3.10.2-2
- Addd sources

* Fri Jun 13 2014 Sergio Pascual <sergiopr@fedoraproject.org> - 3.10.2-1
- New upstream version (3.10.2)

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Dec 05 2013 Sergio Pascual <sergiopr@fedoraproject.org> - 3.10-1
- New upstream version (3.10)
- Fixes format security bug (bz #1037055)

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.9.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Mar 27 2013 Sergio Pascual <sergiopr@fedoraproject.org> - 3.9.6-1
- New upstream version

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.9.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.9.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.9.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Apr 19 2011 Sergio Pascual <sergiopr at fedoraproject.org> 3.9.0-1
- New upstream version

* Mon Dec 13 2010 Sergio Pascual <sergiopr at fedoraproject.org> 3.8.3-2
- EVR bump to allow rebuilding

* Sun Dec 12 2010 Sergio Pascual <sergiopr at fedoraproject.org> 3.8.3-1
- New upstream source
- BZ #563969 fixed upstream, patch removed
- Fixed URL for Source0

* Thu Feb 18 2010 Sergio Pascual <sergiopr at fedoraproject.org> 3.7.2-8
- Patch modified, adding -lcfitsio and -lcext

* Thu Feb 18 2010 Sergio Pascual <sergiopr at fedoraproject.org> 3.7.2-7
- EVR bump to allow rebuilding

* Thu Feb 18 2010 Sergio Pascual <sergiopr at fedoraproject.org> 3.7.2-6
- Patch to fix implicit DSO linking problem, bz #564901

* Wed Feb 17 2010 Sergio Pascual <sergiopr at fedoraproject.org> 3.7.2-5
- Patch to ltdl, fixes security problem CVE-2009-3736, bz #563969

* Wed Nov 04 2009 Sergio Pascual <sergiopr at fedoraproject.org> 3.7.2-4
- Updated build requires

* Tue Nov 03 2009 Sergio Pascual <sergiopr at fedoraproject.org> 3.7.2-3
- Rebuilt for new cpl

* Wed Oct 28 2009 Sergio Pascual <sergiopr at fedoraproject.org> 3.7.2-2
- Fixed configure patch

* Wed Oct 28 2009 Sergio Pascual <sergiopr at fedoraproject.org> 3.7.2-1
- New upstream source

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.6.12-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Fri May 08 2009 Sergio Pascual <sergiopr at fedoraproject.org> 3.6.12-3
- Reverting plugin directory patch. Not working in x86_64

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.6.12-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Dec 22 2008 Sergio Pascual <sergiopr at fedoraproject.org> 3.6.12-1
- New upstream source

* Sat Nov 22 2008 Sergio Pascual <sergiopr at fedoraproject.org> 3.6.8-2
- Summary rewritten

* Sun Apr 06 2008 Sergio Pascual <sergiopr at fedoraproject.org> 3.6.8-1
- New upstream source

* Sat Feb 09 2008 Sergio Pascual <sergiopr at fedoraproject.org> 3.6.6-3
- New upstream source, uses cpl > 4.0

* Thu Sep 13 2007 Sergio Pascual <spr@astrax.fis.ucm.es> 3.6.1-0.3
- Updated license tag to follow Fedora guidelines

* Fri Apr 27 2007 Sergio Pascual <spr@astrax.fis.ucm.es> 3.6.1-0.2
- The recipe dir is predefined in the patch (esorex-pluginpath.patch)

* Thu Apr 26 2007 Sergio Pascual <spr@astrax.fis.ucm.es> 3.6.1-0.1
- Initial spec file.
