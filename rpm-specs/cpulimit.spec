%global commit f4d2682804931e7aea02a869137344bb5452a3cd
%global build_date 20151118

%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global posttag %{build_date}git%{shortcommit}

Name:		cpulimit
Version:	0.2
Release:	10.%{posttag}%{?dist}
Summary:	CPU Usage Limiter for Linux

License:	GPLv2+
URL:		https://github.com/opsengine/cpulimit
Source0:	https://github.com/opsengine/%{name}/archive/%{commit}/%{name}-%{commit}.tar.gz
Epoch:		1

BuildRequires:  gcc
%description
cpulimit is a simple program which attempts to limit the CPU usage of a process
(expressed in percentage, not in CPU time). This is useful to control batch
jobs, when you don't want them to eat too much CPU. It does not act on the nice
value or other scheduling priority stuff, but on the real CPU usage. Also, it
is able to adapt itself to the overall system load, dynamically and quickly.

%prep
%setup -q -n %{name}-%{commit}

%build
%{__make} %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
%{__install} -Dp -m 755 src/cpulimit $RPM_BUILD_ROOT/%{_bindir}/cpulimit

%files
%{!?_licensedir:%global license %%doc}
%{_bindir}/cpulimit
%doc README.md
%license LICENSE

%changelog
* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.2-10.20151118gitf4d2682
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.2-9.20151118gitf4d2682
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.2-8.20151118gitf4d2682
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.2-7.20151118gitf4d2682
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.2-6.20151118gitf4d2682
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.2-5.20151118gitf4d2682
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.2-4.20151118gitf4d2682
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.2-3.20151118gitf4d2682
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.2-2.20151118gitf4d2682
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Nov 18 2015 Christos Triantafyllidis <christos.triantafyllidis@gmail.com> - 1:0.2-1.20151118gitf4d2682
- Updated to version 0.2

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:0.1-3.20140722gitcabeb99
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:0.1-2.20140722gitcabeb99
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Tue Jul 22 2014 Christos Triantafyllidis <christos.triantafyllidis@gmail.com> - 1:0.1-1.20140722gitcabeb99
- Rebuild based on the github sources

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 07 2011 Christos Triantafyllidis <christos.triantafyllidis@gmail.com> 1.1-1
- initial package creation
