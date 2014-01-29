%bcond_with x

Name:           libXrender
Version:        0.9.7
Release:        0
License:        MIT
Summary:        X Rendering Extension library
Url:            http://cgit.freedesktop.org/xorg/lib/libXrender/
Group:          Graphics/X Window System

Source:         %{name}-%{version}.tar.bz2
Source1001: 	libXrender.manifest
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(renderproto) >= 0.9
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xorg-macros) >= 1.8

%if !%{with x}
ExclusiveArch:
%endif

%description
The Xrender library is designed as a lightweight library interface to
the Render extension.

%package devel
Summary:        Development files for the X11 Render Extension library
Group:          Development/Libraries
Requires:       %{name} = %{version}

%description devel
The Xrender library is designed as a lightweight library interface to
the Render extension.

This package contains the development headers for the library found
in %{name}.

%prep
%setup -q
cp %{SOURCE1001} .

%build
%configure --docdir=%_docdir/%{name} --disable-static
make %{?_smp_mflags}

%install
%make_install

%post  -p /sbin/ldconfig

%postun  -p /sbin/ldconfig

%files
%manifest %{name}.manifest
%defattr(-,root,root)
%license COPYING
%{_libdir}/libXrender.so.1*

%files devel
%manifest %{name}.manifest
%defattr(-,root,root)
%{_includedir}/X11/*
%{_libdir}/libXrender.so
%{_libdir}/pkgconfig/xrender.pc
%_docdir/%{name}

%changelog
