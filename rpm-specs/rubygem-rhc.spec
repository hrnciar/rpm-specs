%global gem_name rhc

Summary:       OpenShift Express Client Tools
Name:          rubygem-%{gem_name}
Version:       1.38.7
Release:       9%{?dist}
License:       MIT
URL:           https://openshift.redhat.com/app/express
Source0:       http://rubygems.org/downloads/%{gem_name}-%{version}.gem

# rubygem-rhc only runs on ruby, not jruby or other interpreters
Requires:      ruby
%if 0%{?fc20} || 0%{?el7} || 0%{?el6}
Requires:      ruby(release)
Requires:      rubygem-archive-tar-minitar
Requires:      rubygem-commander >= 4.0
Requires:      rubygem-highline >= 1.6.11
Requires:      rubygem-httpclient >= 2.4
Requires:      rubygem-net-scp  >= 1.1.2
Requires:      rubygem-net-ssh-multi  >= 1.2.0
Requires:      rubygem-open4
Requires:      rubygem-test-unit
%endif
Requires:      git
Requires:      openssh-clients
BuildRequires: rubygems
BuildRequires: rubygems-devel
BuildArch:     noarch
%if 0%{?fc20} || 0%{?el7} || 0%{?el6}
Provides:      rubygem(%{gem_name}) = %{version}
%endif

%description
OpenShift Express Client Tools allows you to create and deploy applications to
the cloud. The OpenShift Express client is a command line tool that allows you
to manage your applications in the cloud.

%package doc
Summary: Documentation for %{gem_name}
Requires: %{name}

%description doc
Documentation for %{name}

%prep
gem unpack %{SOURCE0}

%setup -q -D -T -n %{gem_name}-%{version}

# Modify the gemspec if necessary with a patch or sed
# Also apply patches to code if necessary
# %%patch0 -p1

%if 0%{?fc24} || 0%{?fc25} || 0%{?el7} || 0%{?el6}
gem spec %{SOURCE0} -l --ruby | sed -e 's|commander>, \[\"< 4.3.0\", |commander>, \[|' -e 's|httpclient>, \[\"< 2.7.0\", |httpclient>, \[|'> %{gem_name}.gemspec
%else
gem spec %{SOURCE0} -l --ruby | sed -e 's|commander>.freeze, \[\"< 4.3.0\", |commander>.freeze, \[|' -e 's|httpclient>.freeze, \[\"< 2.7.0\", |httpclient>.freeze, \[|'> %{gem_name}.gemspec
%endif

%build
mkdir -p .%{gem_dir}

# Create the gem as gem install only works on a gem file
gem build %{gem_name}.gemspec

export CONFIGURE_ARGS="--with-cflags='%{optflags}'"
# gem install compiles any C extensions and installs into a directory
# We set that to be a local directory so that we can move it into the
# buildroot in %%install

%gem_install

%check
# Run tests

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a ./%{gem_dir}/* %{buildroot}%{gem_dir}/

# If there were programs installed:
mkdir -p %{buildroot}%{_bindir}
cp -a ./%{_bindir}/* %{buildroot}%{_bindir}

chmod 0755 %{buildroot}%{_bindir}/*
rm -rf %{buildroot}%{gem_instdir}/.yardoc
rm -rf %{buildroot}%{gem_instdir}/spec
rm -rf %{buildroot}%{gem_instdir}/test
rm -rf %{buildroot}%{gem_instdir}/features
rm %{buildroot}%{gem_instdir}/Rakefile

%files
%dir %{gem_instdir}
%dir %{gem_instdir}/bin
%dir %{gem_libdir}
%dir %{gem_instdir}/conf
%doc %{gem_instdir}/COPYRIGHT
%doc %{gem_instdir}/LICENSE
%doc %{gem_instdir}/README.md
%exclude %{gem_cache}
%{gem_spec}
%{gem_instdir}/bin/*
%{gem_libdir}/*
%{gem_instdir}/conf/*
%{gem_instdir}/autocomplete/rhc_bash
%{_bindir}/*


%files doc
%doc %{gem_docdir}

%changelog
* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.38.7-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.38.7-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.38.7-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.38.7-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.38.7-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.38.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu Mar 09 2017 Troy Dawson <tdawson@redhat.com> - 1.38.7-3
- Fixup dependencies for F26+

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.38.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Aug 02 2016 Troy Dawson <tdawson@redhat.com> - 1.38.7-1
- Updated to version 1.38.7
- Fixup dependencies

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.38.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Nov 10 2015 Troy Dawson <tdawson@redhat.com> - 1.38.4-1
- Updated to version 1.38.4

* Tue Sep 15 2015 Troy Dawson <tdawson@redhat.com> - 1.37.1-1
- Updated to version 1.37.1

* Wed Jul 08 2015 Troy Dawson <tdawson@redhat.com> - 1.36.4-1
- Updated to version 1.36.4

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.35.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Apr 17 2015 Troy Dawson <tdawson@redhat.com> - 1.35.3-2
- Fix commander version dependency

* Tue Apr 14 2015 Troy Dawson <tdawson@redhat.com> - 1.35.3-1
- Updated to version 1.35.3

* Tue Mar 03 2015 Troy Dawson <tdawson@redhat.com> - 1.35.1-1
- Updated to version 1.35.1

* Thu Feb 19 2015 Troy Dawson <tdawson@redhat.com> - 1.34.2-2
- Fixed bad changelog date

* Thu Feb 19 2015 Troy Dawson <tdawson@redhat.com> - 1.34.2-1
- Updated to version 1.34.2
- Added Requires: Ruby (#1190847)
- Added if statements so spec will work on EPEL7

* Thu Dec 04 2014 Guillermo Gomez <gomix@fedoraproject.org> - 1.32.2-1
- Updated to version 1.32.2
- Fixed some bogus changelogs dates

* Sun Oct 12 2014 Guillermo Gomez <gomix@fedoraproject.org> - 1.30.2-1
- Updated to version 1.30.2

* Tue Sep 09 2014 Guillermo Gomez <gomix@fedoraproject.org> - 1.29.7-1
- Updated to version 1.29.7

* Tue Jul 22 2014 Guillermo Gomez <gomix@fedoraproject.org> - 1.27.4-1
- Updated to version 1.27.4

* Sun Jun 22 2014 Guillermo Gomez <gomix@fedoraproject.org> - 1.25.3-1
- Updated to version 1.25.3
- New dependency rubygem-net-scp

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.19.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Feb 02 2014 Guillermo Gomez <gomix@fedoraproject.org> - 1.19.5-1
- Updated to version 1.19.5

* Mon Nov 18 2013 Guillermo Gomez <gomix@fedoraproject.org> - 1.18.2-1
- Updated to version 1.18.2

* Mon Nov 18 2013 Guillermo Gomez <gomix@fedoraproject.org> - 1.16.9-1
- Updated to version 1.16.9

* Tue Oct 29 2013 Guillermo Gomez <gomix@fedoraproject.org> - 1.15.6-1
- Updated to version 1.15.6
- rubygem-net-ssh-multi run time dependency addedd

* Wed Sep 25 2013 Guillermo Gomez <gomix@fedoraproject.org> - 1.14.7-1
- Updated to version 1.14.7

* Sun Jul 28 2013 Guillermo Gomez <gomix@fedoraproject.org> - 1.12.4-1
- Updated to version 1.12.4

* Sun Jul 28 2013 Guillermo Gomez <gomix@fedoraproject.org> - 1.11.4-1
- Updated to version 1.11.4

* Wed Jul 10 2013 Guillermo Gomez <gomix@fedoraproject.org> - 1.10.7-1
- Updated to version 1.10.7

* Sun Jun 16 2013 Guillermo Gomez <gomix@fedoraproject.org> - 1.9.6-1
- Updated to version 1.9.6

* Sat May 18 2013 Guillermo Gomez <gomix@fedoraproject.org> - 1.8.9-1
- Updated to version 1.8.9
- Includes a bash autocomplete sample file

* Sat Apr 20 2013 Guillermo Gomez <gomix@fedoraproject.org> - 1.6.8-1
- Updated to version 1.6.8

* Sat Mar 23 2013 Guillermo Gomez <gomix@fedoraproject.org> - 1.5.13-1
- Updated to version 1.5.13
- More spec tweaks for new packaging guidelines for Ruby 2.0.0

* Mon Mar 18 2013 Guillermo Gomez <gomix@fedoraproject.org> - 1.4.8-2
- Spec fixed according new packaging guidelines for Ruby 2.0.0

* Sun Mar 17 2013 Guillermo Gomez <gomix@fedoraproject.org> - 1.4.8-1
- Updated to version 1.4.8
- New dependencies

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Tue Jan 1 2013  Guillermo Gómez <gomix@fedoraproject.org> - 1.2.7-1
- Updated to version 1.2.7
- New runtime dependences added: git, openssh-clients

* Thu Dec 6 2012  Guillermo Gómez <gomix@fedoraproject.org> - 1.1.11-1
- Updated to version 1.1.11

* Mon Nov 12 2012 Guillermo Gómez <gomix@fedoraproject.org> - 1.0.4-2
- New  dependency added (open4)

* Sat Nov 10 2012 Guillermo Gómez <gomix@fedoraproject.org> - 1.0.4-1
- Updated to version 1.0.4
- Excluded cached Gem

* Tue Sep 25 2012 Guillermo Gómez <gomix@fedoraproject.org> - 0.98.16-1
- Updated to version 0.98.16

* Mon Aug 20 2012 Guillermo Gómez <gomix@fedoraproject.org> - 0.96.9-1
- Updated to version 0.96.9

* Thu Jul 19 2012 Guillermo Gómez <gomix@fedoraproject.org> - 0.95.14-2
- Removed some unnecesary dependencies
- Some depedencies adjusted for specific versions

* Wed Jul 18 2012 Guillermo Gómez <gomix@fedoraproject.org> - 0.95.14-1
- Updated to version 0.95.14

* Wed Jun 27 2012 Guillermo Gómez <gomix@fedoraproject.org> - 0.93.19-1
- This versión fixes the rubygem-sshkey dependency

* Wed Jun 13 2012 Guillermo Gómez <gomix@fedoraproject.org> - 0.93.18-2
- rubygem-net-ssh runtime dependency added
- rubygem-archive-tar-minitar runtime dependency added
- rubygem-commander runtime dependency added
- Documentation package requires fixed

* Fri Jun 08 2012 Guillermo Gómez <gomix@fedoraproject.org> - 0.93.18-1
- Updated to version 0.93.18
- Documentation package split

* Sun May 27 2012 Guillermo Gómez <gomix@fedoraproject.org> - 0.92.11-1
- Updated to version 0.92.11

* Wed May 02 2012 Guillermo Gómez <gomix@fedoraproject.org> - 0.91.12-3
- Run time dependency typo fixed

* Wed May 02 2012 Guillermo Gómez <gomix@fedoraproject.org> - 0.91.12-2
- Run time dependency typo fixed
- rubygem-rake run time dependency added

* Tue May 01 2012 Guillermo Gómez <gomix@fedoraproject.org> - 0.91.12-1
- Updated to version 0.91.12
- rubygem-rest-client run time dependency addedd

* Sun Mar 25 2012 Guillermo Gómez <gomix@fedoraproject.org> - 0.88.9-1
- Updated to version 0.88.9

* Thu Mar 15 2012 Guillermo Gómez <gomix@fedoraproject.org> - 0.87.8-1
- Updated to version 0.87.8

* Mon Feb 13 2012 Guillermo Gómez <gomix@fedoraproject.org> - 0.86.7-1
- Updated to version 0.86.7

* Sun Feb 12 2012 Guillermo Gómez <gomix@fedoraproject.org> - 0.84.15-3
- Minor spec file adjustments
- ruby-irb added as a build require

* Fri Feb 03 2012 Vít Ondruch <vondruch@redhat.com> - 0.84.15-2
- Rebuilt for Ruby 1.9.3.

* Fri Jan 20 2012 Guillermo Gómez <gomix@fedoraproject.org> - 0.84.15-1
- Updated to version 0.84.15

* Tue Jan 17 2012 Guillermo Gómez <gomix@fedoraproject.org> - 0.84.13-1
- Updated to version 0.84.13

* Wed Dec 21 2011 Guillermo Gómez <gomix@fedoraproject.org> - 0.83.9-1
- Update to version 0.83.9

* Thu Dec 15 2011 Guillermo Gómez <gomix@fedoraproject.org> - 0.82.18-1
- Update to version 0.82.18

* Thu Dec 01 2011 Guillermo Gómez <gomix@fedoraproject.org> - 0.81.14-2
- Requires fixed to json_pure

* Tue Nov 15 2011 Guillermo Gómez <gomix@fedoraproject.org> - 0.81.14-1
- Update to version 0.81.14

* Wed Nov 02 2011 Guillermo Gómez <gomix@fedoraproject.org> - 0.80.5-1
- Update to version 0.80.5

* Wed Oct 19 2011 Guillermo Gómez <gomix@fedoraproject.org> - 0.79.5-1
- Update to version 0.79.5

* Tue Aug 23 2011 Guillermo Gómez <gomix@fedoraproject.org> - 0.75.9-1
- Update to version 0.75.9

* Tue Aug 02 2011 Guillermo Gómez <gomix@fedoraproject.org> - 0.73.14-1
- Update to version 0.73.14

* Sat Jul 09 2011 Guillermo Gómez <gomix@fedoraproject.org - 0.71.2-2
- Package now owns geminstdir
- User binaries moved to the right place
- %%dir missuse corrected
- Better URL
- Licenced fixed to MIT

* Thu Jun 23 2011 Guillermo Gómez <gomix@fedoraproject.org> - 0.71.2-1
- Initial package
