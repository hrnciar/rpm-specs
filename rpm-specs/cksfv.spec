Name:           cksfv
Version:        1.3.14
Release:        20%{?dist}
Summary:        Utility to manipulate SFV files

License:        GPLv2+
URL:            http://zakalwe.fi/~shd/foss/cksfv
Source0:        http://zakalwe.fi/~shd/foss/%{name}/files/%{name}-%{version}.tar.bz2
Source1:        http://zakalwe.fi/~shd/foss/%{name}/files/%{name}-%{version}.tar.bz2.asc
Source2:        http://zakalwe.fi/~shd/keys/heikki_orsila.pub
BuildRequires:  gcc
BuildRequires:  gnupg2

%description
cksfv is a utility that can create and use SFV files. SFV (Simple File
Verification) files are used to verify file integrity using CRC32
checksums.


%prep
gpg2 --import --import-options import-export,import-minimal %{S:2} > ./gpg-keyring.gpg
gpgv2 --keyring ./gpg-keyring.gpg %{S:1} %{S:0}
%setup -q

# fix rpmlint warnings
iconv -f iso8859-1 -t utf-8 ChangeLog > ChangeLog.conv &&\
touch -r ChangeLog ChangeLog.conv &&\
mv -f ChangeLog.conv ChangeLog


%build
%set_build_flags
# custom configure does not take --libdir spec
./configure \
    --bindir=%{_bindir} \
    --mandir=%{_mandir} \
    --prefix=%{_prefix} \
    --package-prefix=%{buildroot}
make %{?_smp_mflags}


%install
%make_install


%check
make check


%files
%license COPYING
%doc AUTHORS ChangeLog README TODO
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*


%changelog
* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.14-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.14-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.14-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 21 2018 Dominik Mierzejewski <rpm@greysector.net> - 1.3.14-17
- Add BR: gcc for https://fedoraproject.org/wiki/Changes/Remove_GCC_from_BuildRoot
- Verify source tarball GPG signature
- Clean-up and use modern macros to simplify build
- Preserve ChangeLog timestamp

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.14-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.14-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.14-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.14-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.14-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.14-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.14-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.14-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.14-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Apr 10 2014 Dominik 'Rathann' Mierzejewski <rpm@greysector.net> - 1.3.14-7
- drop obsolete specfile parts
- remove redundant variable redirection
- fix license tag

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.14-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.14-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.14-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.14-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.14-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sun Aug 30 2009 Christopher Stone <chris.stone@gmail.com> 1.3.14-1
- Upstream sync
- Remove no longer needed man page patch

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.13-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Feb 23 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.13-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Sep 11 2008 Christopher Stone <chris.stone@gmail.com> 1.3.13-1
- Upstream sync

* Wed Feb 20 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> 1.3.12-3
- Autorebuild for GCC 4.3

* Sat Oct 27 2007 Christohper Stone <chris.stone@gmail.com> 1.3.12-2
- Fix rpmlint issues

* Sat Sep 08 2007 Christopher Stone <chris.stone@gmail.com> 1.3.12-1
- Upstream sync

* Tue Aug 28 2007 Fedora Release Engineering <rel-eng at fedoraproject dot org> - 1.3.11-2
- Rebuild for selinux ppc32 issue.

* Fri Jul 13 2007 Christopher Stone <chris.stone@gmail.com> 1.3.11-1
- Upstream sync

* Tue Mar 27 2007 Christopher Stone <chris.stone@gmail.com> 1.3.10-1
- Upstream sync

* Mon Jan 29 2007 Christopher Stone <chris.stone@gmail.com> 1.3.9-3
- Build with %%{optflags} (bug #225096)
- Remove system macros from spec
- Use $RPM_BUILD_ROOT instead of %%{buildroot}

* Wed Aug 30 2006 Christopher Stone <chris.stone@gmail.com> 1.3.9-2
- FC6 rebuild

* Tue Jun 20 2006 Christopher Stone <chris.stone@gmail.com> 1.3.9-1
- Initial release
