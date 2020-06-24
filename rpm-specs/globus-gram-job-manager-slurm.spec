Name:		globus-gram-job-manager-slurm
%global _name %(tr - _ <<< %{name})
Version:	3.0
Release:	6%{?dist}
Summary:	Grid Community Toolkit - SLURM Job Manager Support

#		The slurm.pm file is BSD, the rest is ASL 2.0
License:	ASL 2.0 and BSD
URL:		https://github.com/gridcf/gct/
Source:		https://repo.gridcf.org/gct6/sources/%{_name}-%{version}.tar.gz
Source8:	README
BuildArch:	noarch

BuildRequires:	perl-generators

Requires:	globus-gram-job-manager >= 13
Requires:	globus-gram-job-manager-scripts >= 4
Requires:	globus-gass-cache-program >= 5
Requires:	globus-gatekeeper >= 9
Requires:	perl(:MODULE_COMPAT_%(eval "`perl -V:version`"; echo $version))
Provides:	%{name}-setup-poll = %{version}-%{release}

Requires(preun):	globus-gram-job-manager-scripts >= 4

%description
The Grid Community Toolkit (GCT) is an open source software toolkit used for
building grid systems and applications. It is a fork of the Globus Toolkit
originally created by the Globus Alliance. It is supported by the Grid
Community Forum (GridCF) that provides community-based support for core
software packages in grid computing.

The %{name} package contains:
SLURM Job Manager Support

%prep
%setup -q -n %{_name}-%{version}

%build
export MPIRUN=no
export SRUN=%{_bindir}/srun
export SBATCH=%{_bindir}/sbatch
export SALLOC=%{_bindir}/salloc
export SCANCEL=%{_bindir}/scancel
export SCONTROL=%{_bindir}/scontrol
%configure --disable-static \
	   --includedir=%{_includedir}/globus \
	   --libexecdir=%{_datadir}/globus \
	   --docdir=%{_pkgdocdir} \
	   --with-perlmoduledir=%{perl_vendorlib}

make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}

# Remove jobmanager-slurm from install dir - leave it for admin configuration
rm %{buildroot}%{_sysconfdir}/grid-services/jobmanager-slurm

# Install README file
install -m 644 -p %{SOURCE8} %{buildroot}%{_pkgdocdir}/README

# Remove license files from pkgdocdir if licensedir is used
%{?_licensedir: rm %{buildroot}%{_pkgdocdir}/GLOBUS_LICENSE}
%{?_licensedir: rm %{buildroot}%{_pkgdocdir}/LICENSE*}

%preun
if [ $1 -eq 0 ]; then
    globus-gatekeeper-admin -d jobmanager-slurm-poll > /dev/null 2>&1 || :
fi

%files
%{_datadir}/globus/globus_gram_job_manager/slurm.rvf
%dir %{perl_vendorlib}/Globus
%dir %{perl_vendorlib}/Globus/GRAM
%dir %{perl_vendorlib}/Globus/GRAM/JobManager
%{perl_vendorlib}/Globus/GRAM/JobManager/slurm.pm
%config(noreplace) %{_sysconfdir}/globus/globus-slurm.conf
%config(noreplace) %{_sysconfdir}/grid-services/available/jobmanager-slurm-poll
%dir %{_pkgdocdir}
%doc %{_pkgdocdir}/README
%{!?_licensedir: %doc %{_pkgdocdir}/GLOBUS_LICENSE}
%{!?_licensedir: %doc %{_pkgdocdir}/LICENSE*}
%{?_licensedir: %license GLOBUS_LICENSE LICENSE*}

%changelog
* Mon Jun 22 2020 Jitka Plesnikova <jplesnik@redhat.com> - 3.0-6
- Perl 5.32 rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu May 30 2019 Jitka Plesnikova <jplesnik@redhat.com> - 3.0-3
- Perl 5.30 rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Sep 13 2018 Mattias Ellert <mattias.ellert@physics.uu.se> - 3.0-1
- Switch upstream to Grid Community Toolkit
- First Grid Community Toolkit release

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.8-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Jun 27 2018 Jitka Plesnikova <jplesnik@redhat.com> - 2.8-7
- Perl 5.28 rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.8-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.8-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Jun 04 2017 Jitka Plesnikova <jplesnik@redhat.com> - 2.8-4
- Perl 5.26 rebuild

* Mon Mar 27 2017 Mattias Ellert <mattias.ellert@physics.uu.se> - 2.8-3
- EPEL 5 End-Of-Life specfile clean-up
  - Remove Group and BuildRoot tags
  - Remove _pkgdocdir macro definition
  - Don't clear the buildroot in the install section
  - Remove the clean section

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sat Sep 03 2016 Mattias Ellert <mattias.ellert@physics.uu.se> - 2.8-1
- GT6 update

* Sun May 15 2016 Jitka Plesnikova <jplesnik@redhat.com> - 2.7-3
- Perl 5.24 rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sun Jul 12 2015 Mattias Ellert <mattias.ellert@fysast.uu.se> - 2.7-1
- GT6 update (Add job dependency RSL to SLURM LRM)

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Jun 03 2015 Jitka Plesnikova <jplesnik@redhat.com> - 2.6-2
- Perl 5.22 rebuild

* Fri May 08 2015 Mattias Ellert <mattias.ellert@fysast.uu.se> - 2.6-1
- GT6 update (Remove GRAM slurm option: SBATCH -l h_cpu)

* Fri Jan 23 2015 Mattias Ellert <mattias.ellert@fysast.uu.se> - 2.5-2
- Implement updated license packaging guidelines

* Thu Nov 13 2014 Mattias Ellert <mattias.ellert@fysast.uu.se> - 2.5-1
- GT6 update

* Mon Oct 27 2014 Mattias Ellert <mattias.ellert@fysast.uu.se> - 2.4-2
- Fix typo in preun scriptlet

* Fri Sep 12 2014 Mattias Ellert <mattias.ellert@fysast.uu.se> - 2.4-1
- Update to Globus Toolkit 6.0
- Drop GPT build system and GPT packaging metadata

* Thu Aug 28 2014 Jitka Plesnikova <jplesnik@redhat.com> - 1.2-5
- Perl 5.20 rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Jan 09 2014 Mattias Ellert <mattias.ellert@fysast.uu.se> - 1.2-3
- Remove unused configure option

* Fri Dec 13 2013 Mattias Ellert <mattias.ellert@fysast.uu.se> - 1.2-2
- Use macros consistently

* Thu Nov 07 2013 Mattias Ellert <mattias.ellert@fysast.uu.se> - 1.2-1
- Now in Globus Toolkit (5.2.5)

* Tue Apr 03 2012 Mattias Ellert <mattias.ellert@fysast.uu.se> - 0.1-2
- Bugfix update

* Thu Mar 01 2012 Emmanouil Paisios <emmanouil.paisios@lrz.de> - 0.1-1
- Created using condor package as a base
