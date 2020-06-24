%global compdir %(pkg-config --variable=completionsdir bash-completion)
%global __requires_exclude .*Acme::Cow.*

Name:           cowsay
Version:        3.04
Release:        14%{?dist}
Summary:        Configurable speaking/thinking cow
License:        GPLv3+
URL:            https://github.com/tnalpgge/rank-amateur-cowsay
Source0:        %{url}/archive/%{name}-%{version}.tar.gz
Source1:        cowsay.bashcomp
Source2:        animalsay
Patch0:         cowsay-3.03-help.patch
Patch1:         mech-and-cow.patch
# these are from https://packages.debian.org/sid/cowsay
Patch2:         cowsay-3.03-debian-01-empty_messages_fix.patch
Patch3:         cowsay-3.03-debian-02-remove_trailing_spaces.patch
Patch4:         cowsay-3.03-debian-utf8_width.patch

BuildArch:      noarch
BuildRequires:  bash-completion
BuildRequires:  perl-generators
Requires:	perl-Encode

%description
cowsay is a configurable talking cow, written in Perl.  It operates
much as the figlet program does, and it written in the same spirit
of silliness.
It generates ASCII pictures of a cow with a message. It can also generate
pictures of other animals.

%prep
%setup -qn rank-amateur-cowsay-cowsay-%{version}
%patch0 -p1 -b .help
%{__sed} -e 's#%PREFIX%/share/cows#%{_datadir}/%{name}#' \
         -e 's#%BANGPERL%#!%{__perl}#' -i %{name}
%{__sed} -e 's#%PREFIX%/share/cows#%{_datadir}/%{name}#' \
         -e 's#/usr/local/share/cows#%{_datadir}/%{name}#' -i %{name}.1

mv cows/mech-and-cow cows/mech-and-cow.cow
%patch1 -p1

%patch2 -p1
%patch3 -p1
%patch4 -p1

%build
echo No need to build anything

%install
# using install.sh is not a good idea so let's make the install manually
mkdir -p $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1,%{_datadir}/%{name},%{_sysconfdir}/bash_completion.d}
cp -p %{name} $RPM_BUILD_ROOT%{_bindir}
cp -p cows/* $RPM_BUILD_ROOT%{_datadir}/%{name}
cp -p %{name}.1 $RPM_BUILD_ROOT%{_mandir}/man1
cp -p %{SOURCE2} $RPM_BUILD_ROOT%{_bindir}

# License issue
rm -f $RPM_BUILD_ROOT%{_datadir}/%{name}/daemon.cow

chmod +x $RPM_BUILD_ROOT%{_bindir}/animalsay
ln -s %{name} $RPM_BUILD_ROOT%{_bindir}/cowthink
ln -s %{name}.1 $RPM_BUILD_ROOT%{_mandir}/man1/cowthink.1
mkdir -p $RPM_BUILD_ROOT%{compdir}/
cp %{SOURCE1} $RPM_BUILD_ROOT%{compdir}/

%files
%doc ChangeLog LICENSE README
%{_bindir}/*
%{_mandir}/man1/cow*
%{_datadir}/%{name}
%exclude %{_datadir}/cowsay/bong.cow
%exclude %{_datadir}/cowsay/sodomized.cow
%exclude %{_datadir}/cowsay/satanic.cow
%(dirname %{compdir})

%changelog
* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.04-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.04-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.04-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.04-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Matthew Miller <mattdm@fedoraproject.org> - 3.04-10
- spec file modernization (no group, no rm -rf)

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.04-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Nov 20 2017 Gwyn Ciesla <limburgher@gmail.com> - 3.04-8
- Drop tastless content entirely.

* Mon Nov 20 2017 Gwyn Ciesla <limburgher@gmail.com> - 3.04-7
- Split out -tasteless, 1515182.

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.04-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.04-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Jan 09 2017 Jon Ciesla <limburgher@gmail.com> - 3.04-4
- Require perl-Encode, BZ 1411168.

* Mon Dec 19 2016 Jon Ciesla <limburgher@gmail.com> - 3.04-3
- Fix license tag, BZ 1350114.

* Wed Dec 14 2016 Jon Ciesla <limburgher@gmail.com> - 3.04-2
- Drop bogus Acme::Cow requirement, BZ 1404804.

* Mon Dec 12 2016 Jon Ciesla <limburgher@gmail.com> - 3.04-1
- 3.04, new upstream location, BZ 1403460.

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.03-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sun Jan 17 2016 Hans Ulrich Niedermann <hun@n-dimensional.de> - 3.03-19
- replace %%define by %%global
- avoid license issue with daemon.cow by not shipping it in RPM

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.03-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Feb 20 2015 Matthew Miller <mattdm@fedoraproject.org> - 3.03-17
- include unicode and formatting fixes from Debian

* Fri Sep 26 2014 Rahul Sundaram <sundaram@fedoraproject.org> - 3.03-16
- fix location of bash completion script
- don't own /etc/bash_completion.d/
- drop redundant buildroot, defattr and clean

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.03-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.03-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jul 17 2013 Petr Pisar <ppisar@redhat.com> - 3.03-13
- Perl 5.18 rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.03-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.03-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.03-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.03-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.03-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.03-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Jul 15 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 3.03-6
- fix license tag to prevent false positive

* Fri May 23 2008 Jon Stanley <jonstanley@gmail.com> - 3.03-5
- Fix license tag

* Tue Oct 09 2007 Michał Bentkowski <mr.ecik at gmail.com> - 3.03-4
- Fix mech-and-cow file (#250844)

* Mon Sep 17 2007 Lubomir Kundrak <lkundrak@redhat.com> - 3.03-3
- Make --help be a bit more sane (#293061)

* Tue Jan 02 2007 Michał Bentkowski <mr.ecik at gmail.com> - 3.03-2
- Use cp -p to keep timestamps
- Fix paths in manpage
- Add animalsay

* Sun Dec 31 2006 Michał Bentkowski <mr.ecik at gmail.com> - 3.03-1
- Initial release
