%define _lto_cflags %{nil}

Name:           libfprint-tod

Version:        1.94.7
Release:        1
Summary:        Toolkit for fingerprint scanner

Provides:       libfprint == 1.94.7
Obsoletes:      libfprint == 1.94.7

License:        LGPLv2+
URL:            http://www.freedesktop.org/wiki/Software/fprint/libfprint
Source0:        https://gitlab.freedesktop.org/3v1n0/libfprint/-/archive/v%{version}+tod1/libfprint-v%{version}+tod1.tar.gz
ExcludeArch:    s390 s390x

BuildRequires:  meson
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  git
BuildRequires:  pkgconfig(glib-2.0) >= 2.50
BuildRequires:  pkgconfig(gio-2.0) >= 2.44.0
BuildRequires:  pkgconfig(gusb) >= 0.3.0
BuildRequires:  pkgconfig(nss)
BuildRequires:  pkgconfig(pixman-1)
BuildRequires:  gtk-doc
BuildRequires:  libgudev-devel
# For the udev.pc to install the rules
BuildRequires:  systemd
BuildRequires:  gobject-introspection-devel
# For internal CI tests; umockdev 0.13.2 has an important locking fix
BuildRequires:  python3-cairo python3-gobject cairo-devel
BuildRequires:  umockdev >= 0.13.2

%description
libfprint offers support for consumer fingerprint reader devices.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%autosetup -S git -n libfprint-v%{version}+tod1

%build
%meson \
  -Dgtk-examples=false \
  -Dinstalled-tests=false \
  --buildtype release
%meson_build

%install
%meson_install

%ldconfig_scriptlets

%check
%meson_test -t 4

%files
%license COPYING
%doc NEWS THANKS AUTHORS README.md
%{_libdir}/*.so.*
%{_libdir}/girepository-1.0/*.typelib
%{_udevhwdbdir}/60-autosuspend-libfprint-2.hwdb
%{_udevrulesdir}/70-libfprint-2.rules

%files devel
%doc HACKING.md
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/libfprint-2.pc
%{_libdir}/pkgconfig/libfprint-2-tod-1.pc
%{_datadir}/gir-1.0/*.gir
%{_datadir}/gtk-doc/html/libfprint-2/

%changelog
%autochangelog
