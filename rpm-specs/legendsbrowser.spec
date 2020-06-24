Name:           legendsbrowser
Version:        1.17.1
Release:        6%{?dist}
Summary:        Java-based legends viewer for Dwarf Fortress

# Main library is under MIT, bundled JS/CSS/etc. (see below) introduce other licenses
License:        MIT and BSD and OFL
URL:            https://github.com/robertjanetzko/LegendsBrowser

Source0:        https://github.com/robertjanetzko/LegendsBrowser/archive/%{version}/%{name}-%{version}.tar.gz

# Patch to adjust the location of the logging and properties file
Patch0:         https://tc01.fedorapeople.org/dwarffortress/legendsbrowser-properties-logging-location.patch

# This is a Java package.
BuildArch:      noarch

BuildRequires:  maven-local

BuildRequires:  dom4j, junit, guava, velocity, apache-commons-logging, javassist
BuildRequires:  reflections

# Bundled JavaScript assets (and their license)
# jquery, jquery-ui, bootstrap are all MIT
# glyphicons-halflings-fonts is MIT too
# d3 is under 3-clause BSD, leaflet is under 2-clause BSD, leaflet plugins are also BSD
# font-awesome is MIT and CC-BY as per http://fontawesome.io/license/
Provides:       bundled(js-jquery) = 1.11.3
Provides:       bundled(js-jquery-ui) = 1.11.4
Provides:       bundled(js-bootstrap) = 3.3.6
Provides:       bundled(js-d3) = 3.5.12
Provides:       bundled(font-awesome) = 4.5.0
Provides:       bundled(js-leaflet) = 1.0.0-beta.2
# Versions unknown, unfortunately.
Provides:       bundled(js-leaflet-opacity-controls)
Provides:       bundled(js-leaflet-minimap-controls)
# Versioning information comes from ttname -a
Provides:       bundled(glyphicons-halflings-regular) = 1.009

# Additional runtime dependencies not listed in pom file
Requires:      mvn(commons-collections:commons-collections)
Requires:      mvn(commons-lang:commons-lang)
Requires:      mvn(org.javassist:javassist)
# Explicit requires for javapackages-tools since legendsbrowser script
# uses /usr/share/java-utils/java-functions
Requires:      javapackages-tools

# Javadoc package.
%package       javadoc
Summary:       Javadoc for %{name}

%description javadoc
This package contains the API documentation for %{name}.

%description
Legends Browser is an multi-platform, open source, java-based legends viewer
for Dwarf Fortress. It works in the browser of your choice and recreates Legends
Mode, with objects accessible as links. Several statistics and overviews are
added.

%prep
%setup -qn LegendsBrowser-%{version}
%patch0 -p1

# Remove irrelevant Maven plugins
%pom_remove_plugin :reflections-maven
%pom_remove_plugin :maven-shade-plugin
%pom_remove_plugin :launch4j-maven-plugin
# Fix manifest entries
%pom_xpath_remove "pom:classpathPrefix"
%pom_xpath_set "pom:addClasspath" false

%build
%mvn_build

%install
%mvn_install

# Install a script to run the application.
%jpackage_script legends.Application "" "" %{name}:commons-cli:commons-logging:dom4j:guava:reflections:velocity:commons-collections:commons-lang:javassist %{name} true

# Adjust the script to make ~/.local/share/legendsbrowser if it doesn't exist.
# This is where our patch puts the properties and log file
sed "s,run,mkdir -p ~/\.local/share/legendsbrowser\nrun," -i %{buildroot}%{_bindir}/legendsbrowser

%files -f .mfiles
%{_bindir}/legendsbrowser
%doc README.md
%license LICENSE.md

%files javadoc -f .mfiles-javadoc
%license LICENSE.md

%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.17.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.17.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.17.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Aug 31 2018 Severin Gehwolf <sgehwolf@redhat.com> - 1.17.1-3
- Add explicit requirement on javapackages-tools. See RHBZ#1600426.

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.17.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Mar 28 2018 Ben Rosser <rosser.bjr@gmail.com> - 1.17.1-1
- Updated to latest upstream release (rhbz#1554100).

* Mon Feb 26 2018 Ben Rosser <rosser.bjr@gmail.com> - 1.17-1
- Updated to latest upstream release (rhbz#1546409).

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.15-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Dec 04 2017 Ben Rosser <rosser.bjr@gmail.com> - 1.15-1
- Updated to latest upstream release, with DF 0.44 support.

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.13-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Jul 18 2017 Ben Rosser <rosser.bjr@gmail.com> - 1.13-1
- Update to latest upstream release, fixing a few bugs.

* Mon Jun 12 2017 Ben Rosser <rosser.bjr@gmail.com> - 1.12.2-1
- Update to latest upstream release.
- Adds support for non-square maps.
- Fixes an issue where legendsbrowser uses the wrong port.

* Mon Jun 05 2017 Ben Rosser <rosser.bjr@gmail.com> - 1.12.1-1
- Update to latest upstream release, 1.12.1, a small bugfix release.
- Fixes an exception while displaying family trees.
- Fixes an exception while displaying event collections.

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.12-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Jul 29 2016 Ben Rosser <rosser.bjr@gmail.com> 1.0.12-3
- Fix versioning information; fontawesome fonts are under OFL.
- Merge Java packaging fixes from gil (pom_xpath_remove and shorter jpackage_script).
- Add missing Requires dependencies that are not automatically picked up.
- Remove unnecessary buildrequires dependency on javapackages-tools.
- Add patch to move log and properties files into ~/.local/share/legendsbrowser/.
- Rewrote Source0 URL to include name-version instead of just version.
- Add (unversioned) bundled provides on leaflet plugins.
- Added license file to javadoc subpackage as well.

* Thu Jul 28 2016 Ben Rosser <rosser.bjr@gmail.com> 1.0.12-2
- Add bundled provides for all javascript/CSS/fonts, update license tag accordingly.
- Remove unnecessary Requires tags.
- Remove unnecessary dir macro from files listing.

* Sat Jul 23 2016 Ben Rosser <rosser.bjr@gmail.com> 1.0.12-1
- Update to latest upstream version

* Fri Jun 17 2016 Ben Rosser <rosser.bjr@gmail.com> 1.0.11-2
- Whoops, typo in jpackage_script; main class is not .main.
- Missing apache-commons-lang dependency in jpackage script.

* Fri May 27 2016 Ben Rosser <rosser.bjr@gmail.com> 1.0.11-1
- Initial package.
