%global         commit      be1657a50dec084be4e736be08d8ca980be46cc5
%global         shortcommit %(c=%{commit}; echo ${c:0:7})
%global         repo        https://github.com/stewartoallen/tonto/
%global         reltag      20150312git%{shortcommit}

Name:           tonto
Version:        1.44
Release:        18.%{reltag}%{?dist}
Summary:        Tools for Pronto programmable remote controls
                # Acme/** is BSD
                # libs/jcomm is GPLv2+,
                # All other Artistic clarified
License:        Artistic clarified and GPLv2+ and BSD
URL:            http://mrallen.com/tonto/
ExcludeArch:    ppc ppc64 s390 s390x ppc64le
Source0:        %{repo}/archive/%{commit}/%{name}-%{shortcommit}.tar.gz

                # Remaining patches after upstreaming what's possible
Patch1:         0001-Disable-Mac-specific-code.patch
Patch2:         0002-Set-javac-target-and-source-to-1.6.patch
Patch3:         0003-Remove-osbaldeston-BMP-support-files.patch
Patch4:         0004-Remove-jarsign-from-build.xml.patch
Patch5:         0005-DriverGenUnix-Use-hardcoded-usr-lib-java-library-pat.patch

                # https://fedorahosted.org/fpc/ticket/507
Provides:       bundled(acme-IntHashtable)
Provides:       bundled(acme-ImageEncoder)
Provides:       bundled(acme-GifEncoder)
Provides:       bundled(acme-GifEncoderHashitem)

BuildRequires:  ant
BuildRequires:  desktop-file-utils
BuildRequires:  gcc
BuildRequires:  java-devel
BuildRequires:  javapackages-local
BuildRequires:  libicns-utils
BuildRequires:  rxtx

Requires:       rxtx
Requires:       hicolor-icon-theme
# Explicit requires for javapackages-tools since tonto script
# uses /usr/share/java-utils/java-functions
Requires:       javapackages-tools


%description
Tonto is a set of tools for the the popular Pronto line of programmable
remote controls manufactured by Philips. The main tool in Tonto is a
graphical editor similar to ProntoEdit. Though ProntoEdit is a capable
editor, it is limited to running on Windows. Tonto is written in Java and
is currently running on Windows, Linux and Mac OSX. Tonto also includes
a developers library and documentation for those interested in either
extending Tonto's capabilities or creating their own CCF files.


%package        javadoc
Summary:        Javadoc for %{name}
BuildArch:      noarch

%description javadoc
Javadoc API documentation for %{name}.


%prep
%setup -qn %{name}-%{commit}
find . \( -name '*.jar' -o -name '*.class' \) -delete
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
mkdir icons
icns2png  --output=icons  -x etc/Tonto.app/Contents/Resources/Tonto.icns


%build
rm -rf jars; mkdir jars
cd jars; ln -sf $(build-classpath RXTXcomm) .;  cd ..
ant all javadoc

export CFLAGS="%{optflags}"
cd libs; sh build-fedora.sh; cd ..

cat > %{name}.desktop << EOF
[Desktop Entry]
Name=%{name}
GenericName=%{name}
Comment=Pronto programmable remote controls tool
Exec=%{name}
Icon=tonto
Terminal=false
Type=Application
Categories=Network;
EOF


%install
install -D libs/libjnijcomm.so %{buildroot}%{_libdir}/%{name}/libjnijcomm.so
%jpackage_script Tonto "" ""  %{name}:RXTXcomm %{name}
%mvn_artifact com.mrallen:%{name}:%{version} jars/%{name}.jar

test -d doc/javadoc && mv doc/javadoc .
%mvn_install -J javadoc

desktop-file-install \
    --dir=%{buildroot}%{_datadir}/applications %{name}.desktop
for size in 16 32 48 128; do
    install -D  icons/Tonto_${size}x${size}x32.png \
        %{buildroot}%{_datadir}/icons/hicolor/${size}x${size}/apps/tonto.png
done

%files -f .mfiles
%dir %{_jnidir}/tonto
%{_libdir}/tonto/*.so
%{_bindir}/tonto
%{_datadir}/icons/hicolor/*/apps/tonto.png
%{_datadir}/applications/tonto.desktop
%license LICENSE
%doc doc/*

%files javadoc -f .mfiles-javadoc
%license LICENSE


%changelog
* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.44-18.20150312gitbe1657a
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.44-17.20150312gitbe1657a
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat Jul 11 2020 Jiri Vanek <jvanek@redhat.com> - 1.44-16.20150312gitbe1657a
- Rebuilt for JDK-11, see https://fedoraproject.org/wiki/Changes/Java11

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.44-15.20150312gitbe1657a
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.44-14.20150312gitbe1657a
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.44-13.20150312gitbe1657a
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Aug 31 2018 Severin Gehwolf <sgehwolf@redhat.com> - 1.44-12.20150312gitbe1657a
- Add explicit requirement on javapackages-tools for tonto script
  which uses java-functions. See RHBZ#1600426.

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.44-11.20150312gitbe1657a
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.44-10.20150312gitbe1657a
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 18 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.44-9.20150312gitbe1657a
- Remove obsolete scriptlets

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.44-8.20150312gitbe1657a
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.44-7.20150312gitbe1657a
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.44-6.20150312gitbe1657a
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.44-5.20150312gitbe1657a
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.44-4.20150312gitbe1657a
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Mar 23 2015 Alec Leamas <leamas.alec@gmail.com> - 1.44-3.20150312gitbe1657a
- Add missing ExcludeArch dut to rxtx dep.

* Thu Mar 19 2015 Alec Leamas <leamas.alec@gmail.com> - 1.44-2.20150312gitbe1657a
- Make javadoc package noarch

* Thu Mar 19 2015 Alec Leamas <leamas.alec@gmail.com> - 1.44-1.20150312gitbe1657a
- Update to latest git sources, merge review commits.
- Flush review changelog.
- Initial release.
