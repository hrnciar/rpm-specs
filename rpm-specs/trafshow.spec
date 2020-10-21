Name:	trafshow
Version:	5.2.3
Release:	25%{?dist}

Summary:	A tool for real-time network traffic visualization
Summary(ru):	Полноэкранное отображение текущего сетевого трафика в сети
License:	BSD
#Url:		http://soft.risp.ru/trafshow/index.shtml
Url:		http://hubbitus.net.ru/trafshow/

# Source:	ftp://ftp.nsk.su/pub/RinetSoftware/%{name}-%{version}.tgz
Source:	http://hubbitus.net.ru/trafshow/trafshow-5.2.3.tgz
# Some hack for known machine type... So, it is not fatal, if it unknown (such as athlon)
Patch0:	trafshow-5.2.3-machinetype_hack_nonfatal.patch
# Upstream dead, and patch related only to new GCC, as I understand
Patch1:	trafshow-5.2.3-elif-without_expression.patch

BuildRequires:  gcc
BuildRequires:	ncurses-devel libpcap-devel autoconf

%description
TrafShow continuously display the information regarding packet traffic
on the configured network interface that match the boolean expression.
It periodically sorts and updates this information.

This funny program may be useful for locating suspicious network
traffic on the net or to evaluate current utilization of the network
interface.

%description -l ru
TrafShow продолжительно отображает информацию о сетевом трафике на
выбранном интерфейсе в соответствии с булевым выражением.
Программа периодически сортирует и обновляет эту информацию.

TrafShow может быть очень полезна для распознавания паразитного сетевого
трафика или для оценки текущей утилизации сетевого интерфейса.

%prep
%setup -q
%patch0 -p0 -b .machinetype
%patch1 -p0 -b .elif

%build
autoconf
%configure

make CCOPT="%optflags" %{?_smp_mflags}

%install
# Install stage in Mekefile incorrect, it try install in root. So, do it manually:
install -d %{buildroot}%{_bindir}
install %{name} %{buildroot}%{_bindir}/
install -d %{buildroot}%{_sysconfdir}
install -m 0644 .%{name} %{buildroot}%{_sysconfdir}/%{name}
install -D -m 0644  %{name}.1 %{buildroot}%{_mandir}/man1/%{name}.1

%files
%doc README CHANGES
%config(noreplace) %{_sysconfdir}/%{name}
%{_bindir}/%{name}
%{_mandir}/man?/*

%changelog
* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.2.3-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.2.3-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 5.2.3-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 5.2.3-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 5.2.3-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 5.2.3-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 5.2.3-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 5.2.3-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 5.2.3-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 5.2.3-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jan 07 2016 Pavel Alexeev <Pahan@Hubbitus.info> - 5.2.3-15
- Fix Russian description appearance (bz#1294793).
- Miinor spec cleanup.

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.2.3-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.2.3-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.2.3-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.2.3-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.2.3-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sun Jul 22 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.2.3-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.2.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.2.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sat Jul 17 2010 Pavel Alexeev <Pahan@Hubbitus.info> - 5.2.3-6
- Changes made due review process. Thank you to Manuel Wolfshant.
- Removed AUTHORS files mention as it absent now.

* Sat Jul 3 2010 Pavel Alexeev <Pahan@Hubbitus.info> - 5.2.3-5
- Add AUTHORS file as suggested by Fabian Affolter.
- Repplace explicit gzip of man by simply copy. It must be compressed automatically (thanks for Fabian Affolter).
- Replace $RPM_BUILD_ROOT by %%buildroot

* Mon Apr 5 2010 Pavel Alexeev <Pahan@Hubbitus.info> - 5.2.3-4
- I was forced to do fork. New URL and Source URL.

* Sun Jul 19 2009 Pavel Alexeev <Pahan@Hubbitus.info> - 5.2.3-3
- Start Fedora Review, thanks to Mads Kiilerich (some changes expired also from comment Fabian Affolter):
- Previous authors of spec mentioned, but changelog history cleaned.
- Comments cleaned slightly.
- Remove INSTALL file from %%doc.
- Add %%{?_smp_mflags} to make command.
- Requires: ncurses redundant, Removed.

* Thu Jul 9 2009 Pavel Alexeev <Pahan@Hubbitus.info> - 5.2.3-2
- Initial try push into Fedora.
- Add Patch0: trafshow-5.2.3-machinetype_hack_nonfatal.patch
- Add Patch1: trafshow-5.2.3-elif-without_expression.patch which is break build.
- Reformat with tabs.
- Add BR autoconf
- Correct buildroot.
- Add %%{?dist} into
- In configure use macroses instead of direct pathes.
- Rewrite installation procedure manually.
- Add file CHANGES to docs.
- Group changed from Monitoring to Applications/Internet
- Add default attributes in %%files section
- Add cleaning buildroot in %%install
- Add ncurses requires.
- Add noreplace option to config.
- Add summary and description in Russian language.

* Mon Oct 30 2006 Pavel Alexeev <pahan@hubbitus.info> - 5.2.3-1
- Package initially imported from altlinux. Thay authors according changlog were:
	Fr. Br. George <george@altlinux.ru>, Konstantin Timoshenko <kt@altlinux.ru>,
	Michael Shigorin <mike@altlinux.ru>, Dmitry V. Levin <ldv@alt-linux.org>
		As it new apoch, old changelog removed.
- Upgrade version to 5.2.3
- Delete Alt patches
- #elif with no expression
