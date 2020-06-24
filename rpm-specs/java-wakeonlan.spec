Name:           java-wakeonlan
Version:        1.0.0
Release:        14%{?dist}
Summary:        Wake On Lan client and java library

License:        LGPLv2
URL:            http://www.moldaner.de/wakeonlan
BuildArch:      noarch
Source0:        %{url}/download/wakeonlan-%{version}.zip

                # Build configuration, no need to upstream.
Patch1:         0001-Update-target-and-source-to-1.5.patch
		# Will upstream
Patch2:         0002-Adding-Swedish-and-Italian-translations.patch


BuildRequires:  ant-junit
BuildRequires:  desktop-file-utils
BuildRequires:  ImageMagick
BuildRequires:  java-devel
BuildRequires:  java-javadoc
BuildRequires:  javapackages-local
BuildRequires:  jpackage-utils
BuildRequires:  jsap

Requires:       jsap
# Explicit requires for javapackages-tools since wakeonlan script
# uses /usr/share/java-utils/java-functions
Requires:       javapackages-tools


%description
wakeonlan is a small OS independent java program that sends 'magic packets'
to wake-on-lan enabled ethernet adapters and motherboards in order to switch
on the called machine. It runs on any machine with an installed 1.4+ java
runtime.

wakeonlan can be used by command line or by a graphical user interface. You
can use wakeonlan as a java library too. It provides a utility class to wake
up remote machines. See wakeonlan javadoc for more information.


%package        javadoc
Summary:        Javadoc for %{name}

%description javadoc
Javadoc API documentation for %{name}.


%prep
%setup -qn wakeonlan-%{version}
%patch1  -p1
%patch2  -p1
find \( -name '*.jar' -o -name '*.class' \) -delete
sed -i '/class-path/I d' etc/META_INF/METAINF.MF
cd lib
ln -s $(build-classpath jsap)  .
ln -s $(build-classpath junit)  .


%build
ant deploy javadoc

cat > %{name}.desktop << EOF
[Desktop Entry]
Name=wakeonlan
GenericName=%{name}
Comment=A wake on lan client
Exec=wakeonlan
Icon=%{name}
Terminal=false
Type=Application
Categories=Network;
EOF


%check
ant test


%install
rm -f %{buildroot}%{_bindir}/wakeonlan
%jpackage_script wol.WakeOnLan "" ""  jsap:java-wakeonlan wakeonlan

mv deploy/doc/javadoc .
%mvn_artifact de.moldaner:wakeonlan:%{version} deploy/wakeonlan.jar
%mvn_install -J javadoc

mkdir -p %{buildroot}%{_datadir}/icons/hicolor/64x64/apps/
convert etc/javaws/wakeonlan64x64.gif -geometry 64x64 \
   %{buildroot}%{_datadir}/icons/hicolor/64x64/apps/%{name}.png

desktop-file-install --vendor="" \
    --dir=%{buildroot}%{_datadir}/applications %{name}.desktop



%files -f .mfiles
%dir %{_datadir}/java/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/64x64/apps/%{name}*
%license deploy/doc/COPYING
%doc deploy/doc/README
%{_bindir}/wakeonlan

%files  -f .mfiles-javadoc javadoc
%license doc/COPYING


%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Aug 31 2018 Severin Gehwolf <sgehwolf@redhat.com> - 1.0.0-11
- Add explicit requirement on javapackages-tools. See RHBZ#1600426.

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 11 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.0.0-8
- Remove obsolete scriptlets

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Mar 02 2015 Alec Leamas <leamas.alec@gmail.com> - 1.0.0-3
- Fix icon name
- Fix wrapper script classpath bug.
- Add Italian and Swedish translations

* Sun Mar 01 2015 Alec Leamas <leamas.alec@gmail.com> - 1.0.0-3
- Handling review remarks:
- Adding desktop file, icon and icon cache snippets.
- Moving javac source + target to 1.6.
- Link javadoc to local files.
- Change BR:
- Claim  /usr/share/jave/java-wakeonlan

* Sun Mar 01 2015 Alec Leamas <leamas.alec@gmail.com> - 1.0.0-2
- Review preparations: check R: and BR:
- Add maven metadata.

* Tue Feb 24 2015 Alec Leamas  <leamas.alec@gmail.com> - 1.0.0-1
- Initial release
