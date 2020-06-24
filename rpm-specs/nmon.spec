Name:           nmon
Version:        16m
Release:        2%{?dist}
Summary:        Nigel's performance Monitor for Linux 

License:        GPLv3
URL:            http://nmon.sourceforge.net
Source0:        https://sourceforge.net/projects/%{name}/files/lmon%{version}.c
Source1:        https://sourceforge.net/projects/%{name}/files/Documentation.txt
# Manpage available from the patch archive:
# http://sourceforge.net/tracker/?func=detail&aid=2833213&group_id=271307&atid=1153693
Source2:        %{name}.1

BuildRequires:  gcc
BuildRequires:  ncurses-devel


%description
nmon is a systems administrator, tuner, benchmark tool, which provides 
information about CPU, disks, network, etc., all in one view.


%prep
%setup -T -c -n %{name}
sed -e "s/\r//" %{SOURCE1} > Documentation.txt
touch -c -r %{SOURCE1} Documentation.txt
cp %{SOURCE0} .


%build
%ifarch ppc %{power64}
  %{__cc} %{optflags} -D JFS -D GETUSER \
     -D LARGEMEM -lncurses -lm lmon%{version}.c -D POWER -o %{name}
%else
  %{__cc} %{optflags} -D JFS -D GETUSER \
     -D LARGEMEM -D X86 -lncurses -lm lmon%{version}.c -o %{name}
%endif


%install
install -D -p -m 0755 %{name} %{buildroot}%{_bindir}/%{name}
install -D -p -m 0644 %{SOURCE2} %{buildroot}%{_mandir}/man1/%{name}.1


%files
%doc Documentation.txt 
%{_mandir}/man1/%{name}.1.*
%{_bindir}/%{name}


%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 16m-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Sep 28 2019 Peter Oliver <rpm@mavit.org.uk> - 16m-1
- Update to version 16m.

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 16k-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jun 27 2019 Peter Oliver <rpm@mavit.org.uk> - 16k-1
- Update to version 16k.

* Wed Apr 17 2019 Peter Oliver <rpm@mavit.org.uk> - 16j-1
- Update to version 16j.

* Wed Feb  6 2019 Peter Oliver <rpm@mavit.org.uk> - 16i-1
- Update to version 16i.

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 16g-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 16g-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 21 2018 Athmane Madjoudj <athmane@fedoraproject.org> - 16g-5
- Add gcc as explicit BR (minimal buildroot change)

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 16g-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 16g-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 16g-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Apr 25 2017 Peter Oliver <rpm@mavit.org.uk> - 16g-1
- Update to version 16g.

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 16f-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue May 31 2016 Peter Oliver <rpm@mavit.org.uk> - 16f-1
- Update to version 16f.

* Sun Apr 10 2016 Peter Oliver <rpm@mavit.org.uk> - 16e-1
- Update to version 16e.

* Sun Feb 28 2016 Peter Oliver <rpm@mavit.org.uk> - 16d-2
- Fix build failure.

* Sun Feb 28 2016 Peter Oliver <rpm@mavit.org.uk> - 16d-2
- Update to version 16d.

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 14i-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 14i-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 14i-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 14i-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Aug 13 2013 Palle Ravn <ravnzon@gmail.com> - 14i-6
- Update to version 14i
- GCC options modified for x86

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 14h-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Jul 18 2013 Palle Ravn <ravnzon@gmail.com> 14h-4
- Update to version 14h

* Mon Mar 18 2013 Palle Ravn <ravnzon@gmail.com> 14g-3
- Streamline download links
- Include manpage from sourceforges patch section
- No longer mark manpage as %%doc
- Only handle manpage in %%install

* Fri Mar 1 2013 Palle Ravn <ravnzon@gmail.com> 14g-2
- Add name macro to source links
- Add name macro to compile and install commands
- Add support for PowerPC compilation
- Remove redundant compile flags
- Changed to arbitrary manpage compression
- Preserve timestamps of Source1

* Mon Feb 25 2013 Palle Ravn <ravnzon@gmail.com> 14g-1
- Initial package
