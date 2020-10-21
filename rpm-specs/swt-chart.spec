Name:           swt-chart
Version:        0.12.0
Release:        4%{?dist}
Summary:        Eclipse SWTChart

License:        EPL-2.0
URL:            https://projects.eclipse.org/projects/science.swtchart
Source0:        https://github.com/eclipse/swtchart/archive/REL-%{version}.tar.gz

# Bundle the old API too for now
# Originally taken from the following URL, but link is now dead:
#   http://sourceforge.net/code-snapshots/svn/s/sw/swt-chart/code/swt-chart-code-312-tags-0.10.0.zip
# TODO remove when linuxtools migrates fully to new API
Source1:        swt-chart-code-312-tags-0.10.0.zip

BuildArch:      noarch

# Upstream Eclipse no longer supports non-64bit arches
ExcludeArch: s390 %{arm} %{ix86}

BuildRequires:  tycho

%description
SWTChart is a light-weight charting component for SWT.

%prep
%setup -q -n swtchart-REL-%{version}

# Bundle the old API too for now - it's a different namespace so there are no clashes
unzip -d old_src %{SOURCE1}
mv old_src/swt-chart-code-312-tags-0.10.0/org.swtchart/src/org/swtchart/ org.eclipse.swtchart/src/org/
rm -rf old_src
sed -i -e '/Export-Package/a\ org.swtchart,' org.eclipse.swtchart/META-INF/MANIFEST.MF

# Target platform and update site are not relevant for RPM builds
%pom_disable_module ../org.eclipse.swtchart.targetplatform org.eclipse.swtchart.cbi
%pom_disable_module ../org.eclipse.swtchart.updatesite org.eclipse.swtchart.cbi
%pom_remove_plugin :target-platform-configuration org.eclipse.swtchart.cbi

# These plugins not relevant for RPM builds
%pom_remove_plugin :maven-pmd-plugin org.eclipse.swtchart.cbi
%pom_remove_plugin :maven-checkstyle-plugin org.eclipse.swtchart.cbi

# Don't build or ship test bundles
%pom_disable_module ../org.eclipse.swtchart.test org.eclipse.swtchart.cbi
%pom_disable_module ../org.eclipse.swtchart.extensions.test org.eclipse.swtchart.cbi

# Drop export bundle not needed at runtime and shrinks the dep tree for this package
%pom_disable_module ../org.eclipse.swtchart.export org.eclipse.swtchart.cbi
%pom_disable_module ../org.eclipse.swtchart.export.test org.eclipse.swtchart.cbi
%pom_disable_module ../org.eclipse.swtchart.feature org.eclipse.swtchart.cbi

%mvn_package "::pom::" __noinstall

%build
# Skip tests due to not working in a headless environment
%mvn_build -j -f -- -f org.eclipse.swtchart.cbi/pom.xml

%install
%mvn_install

%files -f .mfiles
%license LICENSE
%doc README.md CONTRIBUTING.md NEWS.md

%changelog
* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Mar 31 2020 Mat Booth <mat.booth@redhat.com> - 0.12.0-3
- Include %%doc section

* Mon Mar 23 2020 Mat Booth <mat.booth@redhat.com> - 0.12.0-2
- Bundle the old API too for now

* Mon Mar 23 2020 Mat Booth <mat.booth@redhat.com> - 0.12.0-1
- Update to latest upstream release

* Thu Mar 14 2019 Mat Booth <mat.booth@redhat.com> - 0.10.0-7
- Update license tag
- Restrict to same architectures as Eclipse itself
- Don't ship aggregator pom

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Feb 23 2016 Alexander Kurtakov <akurtako@redhat.com> 0.10.0-1
- Update to upstream 0.10 release.

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Jan 15 2015 Mat Booth <mat.booth@redhat.com> - 0.9.0-4
- Fix failure to build from source
- Minor spec file clean ups

* Thu Aug 14 2014 Mat Booth <mat.booth@redhat.com> - 0.9.0-3
- Fix unowned directory

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Feb 27 2014 Roland Grunberg <rgrunber@redhat.com> - 0.9.0-1
- Update to 0.9.0 Release.

* Wed Feb 26 2014 Roland Grunberg <rgrunber@redhat.com> - 0.8.0-9
- Change R:java to R:java-headless (Bug 1068558).

* Wed Oct 23 2013 Roland Grunberg <rgrunber@redhat.com> 0.8.0-8
- Fix Bug 1022166.

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Tue Aug 14 2012 Roland Grunberg <rgrunber@redhat.com> 0.8.0-5
- Remove deprecated tycho.targetPlatform due to p2 support.

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Apr 4 2012 Roland Grunberg <rgrunber@redhat.com> 0.8.0-3
- Use %%{_eclipse_base} from eclipse-platform.

* Mon Apr 2 2012 Roland Grunberg <rgrunber@redhat.com> 0.8.0-2
- Explicitly require java/java-devel >= 1.5 as per manifest.

* Tue Mar 6 2012 Roland Grunberg <rgrunber@redhat.com> 0.8.0-1
- Initial packaging of SWTChart.
